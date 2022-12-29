class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        solution type: optimal
        time complexity: O(n)
        description: iterate array from left to right, keep track of minimum, subtract right from min to calculate profit, store global maximum
        '''
        minimum = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                max_profit = max(prices[i] - minimum, max_profit)
        return max_profit