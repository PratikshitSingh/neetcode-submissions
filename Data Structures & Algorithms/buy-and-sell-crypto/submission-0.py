"""
Idea:
1. iterate from l->r keeping a track of minimum value, thus the maximum profit.

T: O(N)
S: O(1)

Edge case:
1. decreasing value -> 0 profit

Dry run:
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = prices[0]

        for p in prices[1:]:
            if p < min_value:
                min_value = p
            else:
                max_profit = max(max_profit, p-min_value)
        return max_profit