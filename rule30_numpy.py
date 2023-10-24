"""Rule 30: [left XOR (center OR right)]"""

import time
import numpy as np
from typing import Dict

ONE = "██"
ZERO = '  '
mapping: Dict[int, str] = {1: ONE, 0: ZERO}


def rule_30_next_row(
    previous_row: np.ndarray
) -> np.ndarray:
    """Generate next row based on previous row using Rule 30."""
    left: np.ndarray = np.roll(previous_row, 1)
    right: np.ndarray = np.roll(previous_row, -1)
    next_row: np.ndarray = np.logical_xor(left, np.logical_or(previous_row, right))
    return next_row

def print_row(
    row: np.ndarray
) -> None:
    """Convert and print 1s and 0s to the global const assigned at the top of this doc."""
    row_mapped: np.ndarray = np.vectorize(mapping.get)(row)
    row_str: str = "".join(row_mapped)
    print(row_str)

def run_numpy_imp(
    N: int
) -> None:
    """Execute Rule 30 for `N` steps."""
    COL_WIDTH: int = N * 2
    # Initial row has a single '1' in the middle
    row: np.ndarray = np.zeros(COL_WIDTH)
    row[COL_WIDTH // 2] = 1
    print_row(row)

    for _ in range(N):
        row: np.ndarray = rule_30_next_row(row)
        print_row(row)
        # add a delay to more deeply appreciate Rule 30 "unroll"
        time.sleep(0.1)
