class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        if not prices:
            return 0
        result = 0
        while i < len(prices):
            future_prices = prices[i+1:]
            sell = max(future_prices) if future_prices else 0
            profit = -prices[i] + sell if - prices[i] + sell > 0 else 0
            if profit > result:
                result = profit
            i += 1
        return result if result else 0