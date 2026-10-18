"""
Approach-
1. Use l, r pointers, calculate and move the lesser value pointer.

T - O(N)
S - O(1)
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r, water = 0, n-1, 0
        
        while l < r:
            water = max( water, min(heights[l], heights[r])*(r-l) )

            if heights[l] < heights[r]: l+=1
            else: r-= 1
        return water