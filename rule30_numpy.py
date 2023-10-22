import time
import numpy as np

COL_WIDTH = 40
NUM_ROWS = 20
ONE = "█"
ZERO = ' '
mapping = {1: ONE, 0: ZERO}


def rule_30_next_row(previous_row):
    left = np.roll(previous_row, 1)
    right = np.roll(previous_row, -1)
    next_row = np.logical_xor(left, np.logical_or(previous_row, right))
    return next_row

def print_row(row):
    row_mapped = np.vectorize(mapping.get)(row)
    row_str = "".join(row_mapped)
    print(row_str)

def run_numpy_imp():
    # Initial row with a single '1' in the middle
    row = np.zeros(COL_WIDTH)
    row[COL_WIDTH // 2] = 1
    print_row(row)

    for _ in range(NUM_ROWS):
        row = rule_30_next_row(row)
        print_row(row)
        time.sleep(0.2)
