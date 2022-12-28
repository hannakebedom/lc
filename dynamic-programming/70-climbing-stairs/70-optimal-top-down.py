class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        solution type: optimal (top-down)
        time complexity: O(n)
            - the number of ways to get to each step from 1 .. n is calculated once
            - results are memoized in a dict
        description: uses calculated results from previous steps to calculate results for current step
        '''
        def helper(n, cache):
            if n in cache: 
                return cache[n]
            else:
                cache[n] = helper(n - 1, cache) + helper(n - 2, cache)
                return cache[n]
        
        return helper(n, {1 : 1, 2 : 2})

        