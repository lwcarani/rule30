import argparse
from rule30_naive import run_naive_imp
from rule30_numpy import run_numpy_imp

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Rule 30 automaton.")
    parser.add_argument("--np", action="store_true", help="Use NumPy implementation")
    parser.add_argument("--naive", action="store_true", help="Use naive implementation")
    args = parser.parse_args()

    if args.naive:
        print("Running Rule 30 elementary cellular automaton using a naive Python implementation:")
        run_naive_imp()
    else:
        print("Running Rule 30 elementary cellular automaton using a Python implementation with NumPy:")
        run_numpy_imp()