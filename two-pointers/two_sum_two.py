import unittest
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers, left and right, to the first and last indices of the input list
        left, right = 0, len(numbers) - 1

        # Iterate through the list while the left pointer is less than the right pointer
        while left < right:
            # Calculate the sum of the numbers at the current left and right indices
            pair_sum = numbers[left] + numbers[right]

            # If the sum is equal to the target, return the indices of the two numbers
            if pair_sum == target:
                return [left + 1, right + 1]

            # If the sum is greater than the target, decrement the right pointer to move to a smaller number
            elif pair_sum > target:
                right -= 1

            # If the sum is less than the target, increment the left pointer to move to a larger number
            else:
                left += 1

        # If the pointers cross each other without finding a sum equal to the target, return an empty list
        return []


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        # Test case where the target is the sum of the first and last elements
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [1, 2])

        # Test case where the target is the sum of two middle elements
        self.assertEqual(self.solution.twoSum([3, 5, 8, 9, 12], 13), [2, 3])

        # Test case where the target is the sum of two identical elements
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 5, 6], 7), [1, 6])

        # Test case where the target is not the sum of any two elements
        self.assertEqual(self.solution.twoSum([1, 2, 3, 4, 5, 6], 20), [])

        # Test case where the input list is empty
        self.assertEqual(self.solution.twoSum([], 10), [])

        # Test case where the input list has only one element
        self.assertEqual(self.solution.twoSum([5], 5), [])


if __name__ == "__main__":
    unittest.main()
