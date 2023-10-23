"""Rule 30: [left XOR (center OR right)]"""

import time
from typing import List

ONE = "█"
ZERO = ' '

def rule_30_next_row(
    previous_row: List[int]
) -> List[int]:
    """Generate next row based on previous row using Rule 30."""
    next_row = []
    for i in range(len(previous_row)):
        left: int = previous_row[i - 1] if i > 0 else 0
        center: int = previous_row[i]
        right: int = previous_row[i + 1] if i < len(previous_row) - 1 else 0
        next_cell: int = left ^ (center or right)  # [left XOR (center OR right)]
        next_row.append(next_cell)
    return next_row

def print_row(
    row: List[int]
) -> None:
    """Convert and print 1s and 0s to the global const assigned at the top of this doc."""
    row_mapped: List[str] = [ONE if cell else ZERO for cell in row]
    row_str: str = "".join(row_mapped)
    print(row_str)

def run_naive_imp(
    N: int
) -> None:
    """Execute Rule 30 for `N` steps."""
    COL_WIDTH: int = N * 2
    # Initial row has a single '1' in the middle
    row: List[int] = [0] * COL_WIDTH
    row[COL_WIDTH // 2] = 1
    print_row(row)

    for _ in range(N):
        row: List[int] = rule_30_next_row(row)
        print_row(row)
        # add a delay to more deeply appreciate Rule 30 "unroll"
        time.sleep(.1)
