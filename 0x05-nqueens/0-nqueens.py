#!/usr/bin/env python3
import sys

def is_valid(board, row, col):
    # Check if there's a queen in the same column or diagonals
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def NQueen(N):
    def backtrack(row=0):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * N
    backtrack()
    return solutions

def print_solutions(solutions):
    for sol in solutions:
        print([[i, sol[i]] for i in range(len(sol))])

def main():
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
    
    solutions = NQueen(N)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
