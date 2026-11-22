"""
Approach-
1. Find the edge elements
Put nums in set
iterate the array and check for num-1, num+1

T- O(n)
S- O(n)

Dry run-

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums): return 0
        hashset = set()
        for num in nums:
            hashset.add(num)

        min_edge, max_edge = nums[0], nums[0]

        for num in nums:
            if (num-1 not in hashset) and (num+1 in hashset):
                min_edge = num # 3
            
            elif (num+1 not in hashset) and (num-1 in hashset):
                max_edge = num

        return max_edge-min_edge+1
