"""
idea:
1. Naive: sorting T: O(nlogn)
2. Optimized: T: O(nlogk)
    -> make a min heap of size k
    -> store only larget k- elements
    -> the top element of heap will be k-th largest
"""

from heapq import heapify, heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        heapify(min_heap)

        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap, num)
            else:
                popped = heappop(min_heap)
                insert_num = max(num, popped)
                heappush(min_heap, insert_num)
        
        return min_heap[0]