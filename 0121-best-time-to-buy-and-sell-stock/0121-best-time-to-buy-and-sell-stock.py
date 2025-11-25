class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        min_buy = prices[0]

        for price in prices:
            best_profit = max(best_profit, price - min_buy)
            min_buy = min(min_buy, price)
        
        return best_profit