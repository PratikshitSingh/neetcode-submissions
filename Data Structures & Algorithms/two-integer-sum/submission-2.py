"""
Approach-
1. initialize a map
2. if target-nums[i] already exists - return idx, i
3. store value of nums[i], i

T- O(N) iterate the list
S- O(N) store elements of the list
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        for i, num in enumerate(nums):
            try:
                if records[target-num] >= 0:
                    return ([records[target-num], i])
            except:
                records[num] = i
                continue