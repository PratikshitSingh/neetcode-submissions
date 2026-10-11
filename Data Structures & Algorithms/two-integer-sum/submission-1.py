"""
Naive: O(N*N) iterate in nested loop
Time Optimized: sort them and use left, right pointers

T: O(nlogn)
S: O(1)

Better:
1. Use a hashmasp to store the numbers: index
2. find target-current_number in hashset, if exists - true
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i