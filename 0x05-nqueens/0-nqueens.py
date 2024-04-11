#!/usr/bin/python3
"""
N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard
"""
import sys


def is_safe(board, row, col, N):
    """Check if there is a queen in the same column"""
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, N, solutions):
    """method to solve  for nqueens"""
    if row == N:
        solutions.append([[r, c] for r, c in enumerate(board[row-1])])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N, solutions)
            board[row][col] = 0


def print_solutions(N):
    """metho d to print the solution"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    if not solutions:
        print("No solutions found")
        sys.exit(0)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)

    N = sys.argv[1]
    print_solutions(N)
