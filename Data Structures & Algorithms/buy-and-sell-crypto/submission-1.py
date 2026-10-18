class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far, max_profit = prices[0], 0

        for price in prices[1:]:
            if price > min_so_far:
                max_profit = max(max_profit, price-min_so_far)
            else:
                min_so_far = price
        return max_profit