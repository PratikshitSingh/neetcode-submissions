"""
Idea:
1. T: O(n)
2. Naive
    -> Store freq in hashmap & sort on freq descending. T: O(nlogn)
    -> Above can be optimised to T: O(nlogk) using a max heap of size k.

Edge case:

Dry run:
"""

from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        heap = []
        heapify(heap)

        for n, f in freq.items():
            if len(heap) >= k:
                # pop the top item and compare
                lf, ln = heappop(heap)
                if lf < f: 
                    ln = n
                    lf = f
                heappush(heap, (lf, ln))
            else:
                heappush(heap, (f, n)) # deault heap in python is min-heap

        # print(heap)
        return [ n[1] for n in heap ]