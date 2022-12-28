class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        solution type: brute-force
        time complexity: O(2^n)
            - each step has two possible steps (n - 1 & n - 2) from which it can be reached
        description: checks all possible step paths from n to the beginning of the staircase 
        '''
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            '''
            - you can land on any given step by taking either one step or two steps
            - to calculate how many ways one can get to a given step they must the number of ways for them to arrive at the steps from which they can arrive and sum these possiblities
            '''
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)