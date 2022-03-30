# Problem Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Problem Number : 121
# Problem Tag : Array
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 30/3/2022

# Approach 1 (got help from discussion😥)
################################################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        for i in range(len(prices)):
            if sell>=len(prices):
                break
            current_profit = prices[sell]-prices[buy]
            if prices[buy]<prices[sell]:
                max_profit = max(current_profit,max_profit)
            else:
                buy = sell
            sell = sell+1
        return max_profit