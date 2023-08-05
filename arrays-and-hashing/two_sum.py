from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of each number
        num_dict: dict[int, int] = {}

        # Iterate through each number and check if its complement is in the dictionary
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        # If no solution is found, return an empty list
        return []


if __name__ == "__main__":
    # Test the twoSum method with an example
    assert Solution().twoSum(nums=[3, 3], target=6) in [[0, 1], [1, 0]]
