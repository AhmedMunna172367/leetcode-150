import unittest
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        outputs = []
        for i in range(len(nums) - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i] * -1
            left, right = i + 1, len(nums) - 1
            while left < right:
                pair_sum = nums[left] + nums[right]

                if pair_sum == target:
                    outputs.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif pair_sum > target:
                    right -= 1

                else:
                    left += 1

        return outputs


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_three_sum(self):
        # Test case where there is one triplet that sums to zero
        self.assertEqual(
            self.solution.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]]
        )

        # Test case where there are multiple triplets that sum to zero
        self.assertEqual(
            self.solution.threeSum([-1, 0, 1, 2, -1, -4, -1, -1, 3, 4, -2]),
            [[-4, 0, 4], [-4, 1, 3], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]],
        )

        # Test case where there are no triplets that sum to zero
        self.assertEqual(self.solution.threeSum([1, 2, 3, 4, 5]), [])

        # Test case where the input list is empty
        self.assertEqual(self.solution.threeSum([]), [])

        # Test case where the input list has only one element
        self.assertEqual(self.solution.threeSum([5]), [])

        # Test case where the input list has two elements
        self.assertEqual(self.solution.threeSum([1, 2]), [])

        # Test case where the input list has three elements that sum to zero
        self.assertEqual(self.solution.threeSum([-1, 0, 1]), [[-1, 0, 1]])


if __name__ == "__main__":
    unittest.main()
