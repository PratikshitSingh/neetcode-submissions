"""
Idea:
1. T: O(n)
2. Naive
    -> Store freq in hashmap & sort on freq descending. T: O(nlogn), S: O(n+k)
    -> Above can be optimised to T: O(nlogk) using a max heap of size k.
3. O(n) solution is possible using bucket sort


Edge case:

Dry run:
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [ [] for _ in range(len(nums)+1) ]
        for num in nums:
            count[num] += 1
        
        for n, f in count.items():
            freq[f].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1): # elements with 0 freq means they never appeared
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res