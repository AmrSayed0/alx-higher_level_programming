#!/usr/bin/python3

#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    # Check row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def nqueens(board, col, solutions):
    if col == N:
        # Found a solution, append to list of solutions
        queens = [[i, board[i].index(1)] for i in range(N)]
        solutions.append(queens)
        return

    for row in range(N):
        if is_valid(board, row, col):
            board[row][col] = 1
            nqueens(board, col + 1, solutions)
            board[row][col] = 0

if __name__ == "__main__":
    # Check arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize empty board
    board = [[0 for i in range(N)] for j in range(N)]

    # Find solutions
    solutions = []
    nqueens(board, 0, solutions)

    # Print solutions
    for sol in solutions:
        print(sol)
