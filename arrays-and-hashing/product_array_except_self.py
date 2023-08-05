from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize arrays to store the product of all elements to the left and right of the current element
        n = len(nums)
        left = [1] * n
        right = [1] * n

        # Compute the product of all elements to the left of the current element
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # Compute the product of all elements to the right of the current element
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # Compute the product of all elements except the current element
        result = [left[i] * right[i] for i in range(n)]
        return result


if __name__ == "__main__":
    # Test the solution with some example inputs
    solution = Solution()

    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    assert expected == solution.productExceptSelf(nums)

    nums = [-1, 1, 0, -3, 3]
    expected = [0, 0, 9, 0, 0]
    assert expected == solution.productExceptSelf(nums)
