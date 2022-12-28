class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        solution type: optimal (bottom-up)
        time complexity: O(n)
            - bottom-up: we start at the bottom of the staircase and work our way up using the base cases as a starting point
            - results are stored in a list
        description: uses calculated results from previous steps to calculate results for current step
        '''
        cache = [1, 2]

        if n == 1:
            return cache[n - 1]
            
        if n == 2:
            return cache[n - 1]

        for i in range(2, n):
            cache.append(cache[i - 1] + cache[i - 2])
        
        return cache[-1]