from typing import Iterable, List


class Solution:
    def is_valid(self, nums: Iterable[str]) -> bool:
        nums = [i for i in nums if i != "."]
        return len(nums) == len(set(nums))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row
        for row in board:
            if not self.is_valid(row):
                return False

        # Check each column
        for col in zip(*board):
            if not self.is_valid(col):
                return False

        # Check each 3x3 sub-grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_valid(square):
                    return False

        return True


if __name__ == "__main__":
    # fmt: off
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],

        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],

        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    # fmt: on

    print(Solution().isValidSudoku(board))
