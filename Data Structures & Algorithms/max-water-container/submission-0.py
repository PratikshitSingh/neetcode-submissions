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
        for i in range(n-1):
            for j in range(i+1, n):
                max_water = max( max_water, min(heights[i], heights[j])*(j-i) )
        return max_water
