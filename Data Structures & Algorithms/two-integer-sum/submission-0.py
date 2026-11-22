"""
Naive: O(N*N) iterate in nested loop
Time Optimized: sort them and use left, right pointers

T: O(nlogn)
S: O(1)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l<r:
            if nums[l] + nums[r] == target:
                return [l, r]
            
            elif nums[l] + nums[r] < target:
                l += 1
            
            else:
                r -= 1
        