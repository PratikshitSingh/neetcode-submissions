"""
1. Sort O(N logN)
2. then iterate & start a l, r pointers

T - O(N*N)
S - (N)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        nums = sorted(nums)
        print(nums)
        n = len(nums)

        for i in range(n-1):
            l, r = i+1, n-1

            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    results.add((nums[i], nums[l], nums[r]))
                    l += 1

        return [list(ll) for ll in results]