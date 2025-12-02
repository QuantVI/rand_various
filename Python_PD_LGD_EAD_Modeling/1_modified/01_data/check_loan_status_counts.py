# check the counts
# loan_status is at index 16

import sys
import csv

path = ""
tally = {}
cols = []

def preview_csv(path, delimiter="," , enc='utf-8'):
    f = open(path, newline='', encoding=enc, errors='ignore')  # or errors='replace'
    try:
        reader = csv.reader(f, delimiter=delimiter)
        header = next(reader)
        # print("Columns:", header)
        cols = header

        for i, row in enumerate(reader, start=1):
            if tally.get(row[16], 0) == 0:
                tally[ row[16] ] = 1
            else:
                tally[ row[16] ] +=1

    finally:
        f.close()

    return tally

if __name__ == "__main__":
    path = sys.argv[1]
    print("\n\t",path,"\n")

    
    preview_csv(path)
    print(tally)
    
