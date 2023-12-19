# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/26/2023
# Description: a puzzle consisting of a row of squares that contain nonnegative integers, with a zero in the rightmost square

def row_puzzle(row, pos=0, visited=None):
    if visited is None:
        visited = set()         # empty set for memoization

    if pos in visited or pos < 0 or pos >= len(row):        # out of range
        return False

    visited.add(pos)        # add solutions into set

    if row[pos] == 0 and pos == len(row) - 1:       # reaches 0 in the rightmost square
        return True

    return row_puzzle(row, pos + row[pos], visited) or row_puzzle(row, pos - row[pos], visited)         # recursive

"""Example:"""
def main():
    row_1 = [2, 0, 5, 3, 1, 3, 1, 4, 0]
    row_2 = [1, 3, 2, 1, 1, 4, 0]
    row_3 = [2, 1, 0, 3, 8, 4, 0]

    print(row_puzzle(row_1))
    print(row_puzzle(row_2))
    print(row_puzzle(row_3))
if __name__ == "__main__":
    main()