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
        l, r = 0, len(nums)-1

        while l<r:
            m = l + (r-l)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]