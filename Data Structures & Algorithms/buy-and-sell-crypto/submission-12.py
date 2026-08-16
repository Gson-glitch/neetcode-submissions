class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profits = []

        while l <= r and r < len(prices):
            if prices[r] >= prices[l]: # profit
                profit = prices[r] - prices[l]
                profits.append(profit)
                r = r + 1
            else: # loss
                l = r
                r =  r + 1
        if profits:
            return max(profits)
        else:
            return 0



        