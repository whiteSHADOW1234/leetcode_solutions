from typing import List

class Solution:
    def max_profit(self, prices: List[int]) -> int:
        left_idx, max_profit = 0, 0
        
        for right_idx in range(1, len(prices)):
            if prices[right_idx] < prices[left_idx]:
                left_idx = right_idx
            else:
                profit = prices[right_idx] - prices[left_idx]
                max_profit = max(max_profit, profit)
        
        return max_profit
