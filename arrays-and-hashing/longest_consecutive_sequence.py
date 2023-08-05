from typing import List


class Solution:
    # O(nlogn)
    def longestConsecutive(self, nums: List[int]) -> int:
        # If the input list is empty, return 0
        if not nums:
            return 0

        # Sort the input list in ascending order
        nums.sort()

        # Initialize variables to keep track of the current and maximum consecutive sequence lengths
        cur_len = 1
        max_len = 1

        # Iterate through the input list, starting from the second element
        for i in range(1, len(nums)):
            # If the current element is equal to the previous element, skip it
            if nums[i] == nums[i - 1]:
                continue
            # If the current element is one more than the previous element, increment the current sequence length
            elif nums[i] == nums[i - 1] + 1:
                cur_len += 1
            # Otherwise, the current element is not part of the current sequence, so update the maximum sequence length
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1

        # Update the maximum sequence length one last time, in case the longest sequence ends at the end of the input list
        return max(cur_len, max_len)

    # O(n)
    def longest_consecutive(self, nums: List[int]) -> int:
        # If the input list is empty, return 0
        if not nums:
            return 0

        # Create a set of the input list to remove duplicates and improve performance
        nums_set = set(nums)

        # Initialize variables to keep track of the current and maximum consecutive sequence lengths
        cur_len = 1
        max_len = 1

        # Iterate through the set of input numbers
        for num in nums_set:
            # If the current number is the start of a sequence (i.e., the previous number is not in the set), count the length of the sequence
            if num - 1 not in nums_set:
                cur_len = 1
                while num + 1 in nums_set:
                    cur_len += 1
                    num += 1
            # Update the maximum sequence length if the current sequence is longer than the previous maximum
            max_len = max(max_len, cur_len)

        # Return the maximum sequence length
        return max_len


if __name__ == "__main__":
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
