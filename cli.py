"""Rule 30: [left XOR (center OR right)]"""

import argparse
from rule30_naive import run_naive_imp
from rule30_numpy import run_numpy_imp

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Rule 30 automaton.")
    parser.add_argument("--np", action="store_true", help="Use NumPy implementation")
    parser.add_argument("--naive", action="store_true", help="Use naive implementation")
    parser.add_argument("--steps", default=10, help="Specify the number of steps")
    args = parser.parse_args()

    if args.naive:
        print(f"Running Rule 30 cellular automaton for {args.steps} steps (using a naive Python implementation)")
        run_naive_imp(N=int(args.steps))
    else:
        print(f"Running Rule 30 cellular automaton for {args.steps} steps (using a Python implementation with NumPy)")
        run_numpy_imp(N=int(args.steps))