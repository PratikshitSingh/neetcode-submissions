"""
Idea:
1. Naive - Linear iteration of array: O(N)
2. Optimized - variation of binary search
    -> l, r
    -> m
    -> a[m] == target
    -> a[l] < a[m]: left half is sorted. 
        target lies between them => search only left subarray
        else => search only right subarray
    
    -> else:right subarray is sorted:
        target lies between them => search only right subarray
        else => search only left subarray


target = 1
3, 4, 5, 6, 1, 2
         l      r

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m = l + (r-l)//2

            if nums[m] == target: return m

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1