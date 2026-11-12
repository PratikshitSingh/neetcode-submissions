"""
Method-
1. l, m, r
2. if a[m]<a[r] => r = m
3. else a[m]>a[r] => l = m+1

T: O(log n) - binbary search
S: O(1)

Dry run:
[3,4,5,6,1,2]
       m lr  

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l<r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
        return nums[r]