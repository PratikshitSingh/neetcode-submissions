"""
Idea:
1. Naive - O(N) iterate through the array & a[i]<a[i+1] => the rotation
2. Optimized - Use binary search
3. l, r
    -> a[m] < a[r]: r = m-1
    -> a[l] < a[m]: l = m+1

T: O(logn)
S: O(1)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = l + (r-l)//2
            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m- 1
        return res