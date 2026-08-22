class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        if not prices:
            return 0
        results = []
        while i < len(prices):
            future_prices = prices[i+1:]
            sell = max(future_prices) if future_prices else 0
            results.append(-prices[i] + sell if - prices[i] + sell > 0 else 0)
            i += 1
        return max(results) if results else 0