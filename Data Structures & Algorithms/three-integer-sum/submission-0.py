"""
Idea:
1. Sort the array.
2. for every i: 0->n-2 : iterate with l, r pointers

T: O(N*N + NlogN) = O(N*N)
S: O(1)

Dry run:
[-4,-1,-1,0,1,2]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n-2):
            l = i+1
            r = n-1
            # print([nums[i], nums[l], nums[r]])

            while l<r:
                if nums[i]+nums[l]+nums[r] == 0:
                    res.add( (nums[i], nums[l], nums[r]) )
                    l += 1
                elif nums[i]+nums[l]+nums[r] < 0:
                    l+=1
                elif nums[i]+nums[l]+nums[r] > 0:
                    r-=1
        return [list(r) for r in res]

