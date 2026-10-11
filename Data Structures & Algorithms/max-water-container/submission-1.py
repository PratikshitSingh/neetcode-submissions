"""
Idea:

naive:
1. Check combination of every 1 heights T: O(N*N)

Optimized:

"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        n = len(heights)
        l, r = 0, n-1

        while l < r:
            max_water = max( max_water, min(heights[l], heights[r])*(r-l) )

            if heights[l] < heights[r]: l+=1
            else: r-=1
        return max_water
