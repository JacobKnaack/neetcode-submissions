class Solution:
    def isValley(self, position: int, prices: List[int]) -> bool:
        current = prices[position]
        next = None
        previous = None
        if position + 1 < len(prices):
            next = prices[position + 1]
        if position > 0:
            previous = prices[position - 1]
        if previous is None and next is not None and current < next:
            return True
        if previous is not None and next is not None and current <= previous and current < next:
            return True
        return False

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # Search each value for valleys
        for i in range(len(prices)):
            is_valley = self.isValley(i, prices)
            if is_valley:
                # search for max_profit
                for j in range(i + 1, len(prices)):
                    current_price = prices[i]
                    profit = prices[j] - current_price
                    if profit > max_profit:
                        max_profit = profit

        return max_profit