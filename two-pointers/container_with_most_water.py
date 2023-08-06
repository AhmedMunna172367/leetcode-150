import unittest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_area(self):
        # Test case where the maximum area is in the middle of the input list
        self.assertEqual(self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

        # Test case where the maximum area is at the edges of the input list
        self.assertEqual(self.solution.maxArea([1, 1]), 1)
        self.assertEqual(self.solution.maxArea([1, 2]), 1)
        self.assertEqual(self.solution.maxArea([2, 1]), 1)

        # Test case where all heights are the same
        self.assertEqual(self.solution.maxArea([5, 5, 5, 5, 5]), 20)

        # Test case where the input list is empty
        self.assertEqual(self.solution.maxArea([]), 0)

        # Test case where the input list has only one element
        self.assertEqual(self.solution.maxArea([5]), 0)

        # Test case where the input list has two elements
        self.assertEqual(self.solution.maxArea([5, 10]), 5)


if __name__ == "__main__":
    unittest.main()
