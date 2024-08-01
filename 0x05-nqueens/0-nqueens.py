#!/usr/bin/python3
""" N QUEENS ALGORITHM"""
import sys


class NQueen:
    """ Constructor to initialize the board size
    and other variables """

    def __init__(self, n):
        """ Global Variables """
        self.n = n
        self.x = [0 for i in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """ Function to check if a queen can be placed
        at position (k, i)
        """

        # j checks from 1 to k - 1 (Up to previous queen)
        for a in range(1, k):
            # There is already a queen in column
            # or a queen in same diagonal
            if self.x[a] == i or \
               abs(self.x[a] - i) == abs(a - k):
                return 0
        return 1

    def nQueen(self, k):
        """ Recursive function to solve the
        N Queens problem
        """
        # a goes from column 1 to column n (1st column is 1st index)
        for a in range(1, self.n + 1):
            if self.place(k, a):
                # Queen can be placed in i column
                self.x[k] = a
                if k == self.n:
                    # If all queens are placed, add the
                    # solution to the result list
                    solution = []
                    for a in range(1, self.n + 1):
                        solution.append([a - 1, self.x[a] - 1])
                    self.res.append(solution)
                else:
                    # Need to place more Queens
                    self.nQueen(k + 1)
        return self.res


# Main

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

B = sys.argv[1]

try:
    B = int(B)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if B < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(B)
res_grap = queen.nQueen(1)

for a in res_grap:
    print(a)
