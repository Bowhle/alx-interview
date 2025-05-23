#!/usr/bin/python3
"""Solves the N Queens problem using backtracking."""
import sys

# Check for correct number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

# Check if argument is a number
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

# Check if N is at least 4
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, row=0, cols=[], diag1=[], diag2=[]):
    """
    Generates all possible solutions for the N Queens problem.
    Uses backtracking to place queens row by row.
    """
    if row < n:
        for col in range(n):
            if col not in cols and row + col not in diag1 and row - col not in diag2:
                yield from queens(n, row + 1, cols + [col], diag1 + [row + col], diag2 + [row - col])
    else:
        yield cols


def solve(n):
    """
    Prints all solutions in the required format.
    Each solution is a list of [row, col] positions for each queen.
    """
    for solution in queens(n):
        print([[row, col] for row, col in enumerate(solution)])


solve(n)
