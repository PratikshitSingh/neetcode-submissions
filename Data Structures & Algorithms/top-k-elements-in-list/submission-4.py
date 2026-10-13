"""
Approach-
1. 

T - O(n)
S - O(n)

Dry run-

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = Counter(nums) # O(n)
        freq_map = [[] for _ in range(len(nums)+1)]

        for key, value in mapper.items():
            freq_map[value].append(key)

        results = []
        for values in reversed(freq_map):
            results.extend(values)
            k -= len(values)
            if k <= 0:
                print(results)
                return results

        