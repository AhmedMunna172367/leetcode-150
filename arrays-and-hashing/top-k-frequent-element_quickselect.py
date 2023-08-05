# TODO: Quickselect, need to have a deeper understanding of this algorithm
# link: https://leetcode.com/problems/top-k-frequent-elements/editorial/

import random
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        count = Counter(nums)

        # Get a list of the unique numbers
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            # Get the frequency of the pivot number
            pivot_frequency = count[unique[pivot_index]]

            # Move the pivot number to the end of the list
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # Move all numbers with a lower frequency to the left of the pivot
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # Move the pivot number to its final position
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            # Base case: the list has only one element
            if left == right:
                return

            # Choose a random pivot index
            pivot_index = random.randint(left, right)

            # Partition the list around the pivot
            pivot_index = partition(left, right, pivot_index)

            # If the pivot is the kth smallest element, we're done
            if k_smallest == pivot_index:
                return
            # If the kth smallest element is to the left of the pivot, recurse on the left side
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # If the kth smallest element is to the right of the pivot, recurse on the right side
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        # Use quickselect to find the kth smallest element
        n = len(unique)
        quickselect(0, n - 1, n - k)

        # Return the k most frequent numbers
        return unique[n - k :]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
