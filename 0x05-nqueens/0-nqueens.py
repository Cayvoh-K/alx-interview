#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
"""

import sys


def n_queens(n):
    def backtrack(col, diag1, diag2):
        nonlocal n, solutions
        row = len(col)
        if row == n:
            solutions.append(col)
        for i in range(n):
            if i not in col and row-i not in diag1 and row+i not in diag2:
                backtrack(col+[i], diag1+[row-i], diag2+[row+i])
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    backtrack([], [], [])
    for sol in solutions:
        print([[i, sol[i]] for i in range(n)])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
n_queens(n)
