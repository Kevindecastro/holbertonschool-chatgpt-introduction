#!/usr/bin/python3
import sys


def print_arguments():
    """
    Print all arguments passed to the script except the script name.

    Parameters:
        None

    Returns:
        None
    """
    for arg in sys.argv[1:]:
        print(arg)


if __name__ == "__main__":
    print_arguments()
