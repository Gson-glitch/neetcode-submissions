class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, max_profit = 0, 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)

        return max_profit

        