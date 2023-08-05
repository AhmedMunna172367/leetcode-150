import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        # Count the frequency of each number
        count = collections.Counter(nums)

        # Create a min heap of the k most frequent numbers
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)
        top_k = [heapq.heappop(heap)[1] for _ in range(k)]

        return top_k

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        # Count the frequency of each number
        count = collections.Counter(nums)

        # Get the k most frequent numbers using nlargest
        top_k = heapq.nlargest(k, count.keys(), key=count.get)  # type:ignore

        return top_k


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
    print(Solution().topKFrequent2(nums, k))
