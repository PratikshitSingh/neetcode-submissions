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

        longest_diff = 1
        for num in nums:
            diff = 1
            if (num-1 not in hashset) and (num+1 in hashset):
                while num+1 in hashset:
                    diff += 1
                    num += 1
                longest_diff = max(diff, longest_diff)

        return longest_diff
