import time

ONE = "█"
ZERO = ' '

def rule_30_next_row(previous_row):
    next_row = []
    for i in range(len(previous_row)):
        left = previous_row[i - 1] if i > 0 else 0
        center = previous_row[i]
        right = previous_row[i + 1] if i < len(previous_row) - 1 else 0
        next_cell = left ^ (center or right)
        next_row.append(next_cell)
    return next_row

def print_row(row):
    for cell in row:
        print(ONE if cell else ZERO, end="")
    print()

def run_naive_imp(
    N: int
):
    COL_WIDTH = N * 2
    # Initial row has a single '1' in the middle
    row = [0] * COL_WIDTH
    row[COL_WIDTH // 2] = 1
    print_row(row)

    for _ in range(N):
        row = rule_30_next_row(row)
        print_row(row)
        # add a delay to more deeply appreciate Rule 30 "unroll"
        time.sleep(.1)
