# This script works.

NOTE_01 = """
Reducing the filesize of a Lending Club data CSV so that it can be
more easily uploaded to GitHub.

    The Zipped filesize is   : 347 MB  ( i.e. 347 191 KB )
    The Unzipped filesize is : 1.61 GB ( i.e. 1 161 520 KB )"""

ORIGINAL_FILE_LOCATION = "https://www.kaggle.com/datasets/adarshsng/"
ORIGINAL_FILE_LOCATION += "lending-club-loan-data-csv?select=loan.csv"

LOAN_STATUS_COUNTS = """
The 1.1-1.6 GB file from that locatin above has the following loan statuses
and counts. (Or file has 145 columns not 75, should be 
from the same source :  Lending Club

    {'Current': 919695, 
     'Fully Paid': 1041952, 
     'Late (31-120 days)': 21897, 
     'In Grace Period': 8952, 
     'Charged Off': 261655, 
     'Late (16-30 days)': 3737, 
     'Default': 31, 
     'Does not meet the credit policy. Status:Fully Paid': 1988, 
     'Does not meet the credit policy. Status:Charged Off': 761
     }
We should keep charge offs and defaults for sure. Late is also useful."""


# How to call this file at the command line
USAGE = "see below"

import sys
import os # to get the original filesize
import csv # to read csv line-by-line and save memory
import random # for sampling lines from the original


# Set these to empty. They will be changing later.
path = ''
outp = ''


status_counts = {}
total_rows = 0
header_idx = None
delim = ","


def do_stuff():
    global total_rows

    # Get original file size
    file_size = os.path.getsize(path)
    print(f"\t---> The original file is : {file_size} bytes")

    # First streaming pass - To Collecy Stats
    # - count rows
    # - count each loan_statis
    # - estimate average row size

    f = open(path, newline='', encoding='utf-8', errors='ignore')
    try:
        reader = csv.reader(f, delimiter=delim)
        header = next(reader)
        header_idx = header.index('loan_status')

        for row in reader:
            total_rows = total_rows + 1
            status = row[header_idx]
            status_counts[status] = status_counts.get(status, 0) + 1

        # After the loop finishes, set the average
        avg_row_bytes = file_size / total_rows
        
        print(f"\n\tTotal rows:\t {total_rows}")
        print(f"\n\t{status_counts}\n")
        # print(f"\n\t")

    finally:
        f.close()


    # Results
    # - total_rows : exact count
    # - status_counts : dictionary of exact distribution
    # - avg_row_bytes = file_size / total_rows
    # --------

    # Compute Target Rows
    desired_mb = mega
    target_bytes = desired_mb * 1_048_576
    target_rows = int(target_bytes / avg_row_bytes)
    
    
    print("desired_mb, target_bytes, target_rows")
    print(desired_mb, target_bytes, target_rows)

    # Adjust Ratios for Excluded Statuses
    exclude = {'Does not meet the credit policy. Status:Fully Paid',
               'Does not meet the credit policy. Status:Charged Off'}

    kept_total = sum(ct for st, ct in status_counts.items() if st not in exclude)
    adjusted_ratios = {
        st: ct / kept_total for st, ct in status_counts.items()
        if st not in exclude
        }

    # Compute per-status quotas
    quotas = {st: int(ratio * target_rows)
              for st, ratio in adjusted_ratios.items()}

    # Second streaming pass - weighted reservoir sampling
    reservoirs = {st: [] for st in quotas}
    seen = {st: 0 for st in quotas}

    f = open(path, newline='', encoding='utf-8', errors='ignore')

    try:
        reader = csv.reader(f, delimiter=delim)
        header = next(reader)

        for row in reader:
            status = row[header_idx]
            if status in exclude: continue

            seen[status] += 1
            q = quotas[status]

            if len(reservoirs[status]) < q:
                reservoirs[status].append(row)
            else:
                # replace with probability q / seen[status]
                if random.random() < q / seen[status]:
                    replace_idx = random.randrange(q)
                    reservoirs[status][replace_idx] = row

    finally:
        f.close()


    # Writing the result
    out = open(outp, 'w', newline='', encoding='utf-8')

    writer = csv.writer(out)
    writer.writerow(header)

    for rows in reservoirs.values(): writer.writerows(rows)

    out.close()




# Now run the file.

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("""The way to use this is:
    > python thisFile.py inputFile.csv outputFile.csv MegabytesOutputSize

e.g.

    > python createsmall.py loans.csv smallerloans.csv 400
    
    ... where 400 refers to megabytes
""")
        print(f"\nYou passed in:\t{sys.argv}")
        #print(len(sys.argv))
    
    else:
        path = sys.argv[1]
        outp = sys.argv[2]
        mega = int(sys.argv[3])
        print("\n\t",path,"\n",sys.argv)
        
        do_stuff()
