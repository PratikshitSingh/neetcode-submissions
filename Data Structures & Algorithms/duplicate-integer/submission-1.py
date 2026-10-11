"""
Approach - 
1. Start an empty set.
2. Iterate & insert each no in set - if it already exists => duplicate

Edge Cases - empty array

T- O(N)
S- O(N)

Dry run-


"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set()

        for num in nums:
            if num in uniques: return True
            uniques.add(num)
        return False