# Reducing the filesize of a Lending Club data CSV so that it can be
  # more easily uploaded to GitHub.

# The Zipped filesize is   : 347 MB  ( i.e. 347 191 KB )
# The Unzipped filesize is : 1.61 GB ( i.e. 1 161 520 KB )
ORIGINAL_FILE_LOCATION = "https://www.kaggle.com/datasets/adarshsng/"
ORIGINAL_FILE_LOCATION += "lending-club-loan-data-csv?select=loan.csv"

# How to call this file at the command line
USAGE = """
python crate_small_datafile.py \
    --input loan.csv \
    --output loan_small.csv \
    --keep-status "Fully Paid" "Current" \
    --target-size-mb 600

* --keep-status  list of statuses to retain
    Use --drop-status instead if you prefer to specift what to exlcude

* --target-size-mb  optional. If omitted the script writes all filtered rows

* --seed  optional integer for reproducible random sampling.
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
    leep_status_set: set,
    drop_status_set: set,
    target_bytes: int,
    sample_chunk: int = 100_000,
    ) -> float:
    
