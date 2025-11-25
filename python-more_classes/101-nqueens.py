#!/usr/bin/python3
"""
N Queens puzzle solver
"""
import sys


def print_usage_and_exit(message, status):
    print(message)
    sys.exit(status)


if len(sys.argv) != 2:
    print_usage_and_exit("Usage: nqueens N", 1)

N_str = sys.argv[1]

if not N_str.isdigit():
    print_usage_and_exit("N must be a number", 1)

N = int(N_str)

if N < 4:
    print_usage_and_exit("N must be at least 4", 1)


def is_safe(board, row, col):
    """Check if the queen can be placed at board[row] = col"""
    for r in range(row):
        if board[r] == col or \
           abs(board[r] - col) == abs(r - row):
            return False
    return True


def solve_nqueens(row, board, solutions):
    """Recursively place queens"""
    if row == N:
        # Convert board to required format
        solution = [[i, board[i]] for i in range(N)]
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(row + 1, board, solutions)


solutions = []
solve_nqueens(0, [0] * N, solutions)

for sol in solutions:
    print(sol)
