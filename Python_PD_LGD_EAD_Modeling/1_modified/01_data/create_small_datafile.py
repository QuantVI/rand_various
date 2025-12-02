# Reducing the filesize of a Lending Club data CSV so that it can be
  # more easily uploaded to GitHub.

# The Zipped filesize is   : 347 MB  ( i.e. 347 191 KB )
# The Unzipped filesize is : 1.61 GB ( i.e. 1 161 520 KB )
ORIGINAL_FILE_LOCATION = "https://www.kaggle.com/datasets/adarshsng/"
ORIGINAL_FILE_LOCATION += "lending-club-loan-data-csv?select=loan.csv"

# How to call this file at the command line
USAGE = """
python create_small_datafile.py \
    --input loan.csv \
    --output loan_small.csv \
    --keep-status "Fully Paid" "Current" \
    --target-size-mb 600

* --keep-status  list of statuses to retain
    Use --drop-status instead if you prefer to specift what to exlcude

* --target-size-mb  optional. If omitted the script writes all filtered rows

* --seed  optional integer for reproducible random sampling.
"""

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
We should keep charge offs and defaults for sure. Late is also useful.
"""


import argparse
import csv
import os
import random
import sys
from pathlib import Path

msg = {
    "desc":"""Shrink a LendingClub CSV by filtering loan_status
and optionally sampling to reach a target file size.""",
    "inp": "Path to the original loan.csv",
    "out":"Path for the reduced CSV",
    "keep":"Loan status values to keep (all others are dropped).",
    "drop":"Loan status values to srop (all others are kept).",
    "targ":"Desired maximum size of the output file in megabytes.",
    "seed":"Random seed for reproducible sampling.",
    "samp":"""Scab a subset of the file to estimate how many rows
survive the status filter, then compute a sampling probability that
should bring the final size close to target_bytes.""",
    "verr":"create_small_datafile.py"
    }


def parse_args():
    parser = argparse.ArgumentParser(description=msg["desc"])
    
    parser.add_argument("--input", required =True, help=msg["inp"])
    parser.add_argument("--output", required=True, help=msg["out"])

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--keep-status", nargs="+", help=msg["keep"])
    group.add_argument("--drop-status", nargs="+", help=msg["drop"])

    parser.add_argument("--target-size-mb",type=int,help=msg["targ"])
    parser.add_argument("--seed",type=int,default=42,help=msg["seed"])

    return parser.parse_args()


def estimate_sampling_rate(
    input_path : Path,
    keep_status_set: set,
    drop_status_set: set,
    target_bytes: int,
    sample_chunk: int = 100_000,
    ) -> float:
    """Scan a subset of the file to estimate how many rows survive
    the status filter, then compute a sampling probability that should
    bring the final size close to target_bytes."""

    total_rows = 0
    kept_rows = 0
    with input_path.open(newline="", encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i >= sample_chunk:
                break
            total_rows +=1
            status = row["loan_status"]
            if keep_status_set and status not in keep_status_set:
                continue
            if drop_status_set and status in drop_status_set:
                continue
            kept_rows += 1

    if kept_rows == 0:
        raise ValueError("No rows match the status filter in the sample.")

    # Approximate size per kept row (including newline)
    avg_row_bytes = os.path.getsize(input_path) / total_rows
    estimated_kept_bytes = kept_rows * avg_row_bytes

    # Desired proportion of kept rows to reach target size
    proportion = min(1.0, target_bytes / estimated_kept_bytes)
    return proportion


def shrink_csv(
        input_path: Path,
        output_path: Path,
        keep_status: list | None,
        drop_status: list | None,
        target_size_mb: int | None,
        seed: int,
        ):
    random.seed(seed)
    
    keep_set = set(keep_status) if keep_status else set()
    drop_set = set(drop_status) if drop_status else set()
    
    # If we have a size target, estimate a sampling probability first
    sample_prob = 1.0
    if target_size_mb:
        target_bytes = target_size_mb * 1024 * 1024
        sample_prob = estimate_sampling_rate(
            input_path, 
            keep_set, 
            drop_set, 
            target_bytes)
        # Clamp to a sensible range
        sample_prob = max(0.01, min(sample_prob, 1.0))
        print(f"Estimated sample probability: {sample_prob:.4f}")
        
    with input_path.open(newline="", encoding='utf-8', errors='ignore') as fin, \
    output_path.open("w", newline="", encoding='utf-8', errors='ignore') as fout:
        reader = csv.DictReader(fin)
        writer = csv.DictWriter(fout, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        kept = 0
        total = 0
        for row in reader:
            total += 1
            status = row["loan_status"]
            if keep_set and status not in keep_set:
                continue
            if drop_set and status in drop_set:
                continue
            if random.random() > sample_prob:
                continue
            writer.writerow(row)
            kept += 1
    
    print(f"Finished. Kept {kept:,} of {total:,} rows ({kept/total:.2%}).")
    final_size = output_path.stat().st_size / (1024 * 1024)
    print(f"Output file size: {final_size:.1f} MB")


def main():
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    
    if not input_path.is_file():
        sys.exit(f"Error: input file '{input_path}' not found.")
    
    shrink_csv(
        input_path=input_path, 
        output_path=output_path, 
        keep_status=args.keep_status, 
        drop_status=args.drop_status, 
        target_size_mb=args.target_size_mb, 
        seed=args.seed
        )

if __name__ == "__main__":
    main()