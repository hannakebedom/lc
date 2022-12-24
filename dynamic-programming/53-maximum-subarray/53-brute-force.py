from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        solution type: brute-force
        time complexity: O(n^2)
        description: visits every subarray, for each subarray calculates sum & checks if it's the greatest sum overall 
        resources:
        - https://www.youtube.com/watch?v=2MmGzdiKR9Y&ab_channel=BackToBackSWE
        '''
        overall_max = float('-inf')
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                overall_max = max(total, overall_max)
        return overall_max