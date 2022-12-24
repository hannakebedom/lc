class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        solution type: optimal
        time complexity: O(n)
        description: at each index check if the max sum is carried over from the previous subarray or begins at the current index (kadane's algorithm)
        '''
        
        curr_max = nums[0]
        total_max = curr_max

        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            total_max = max(total_max, curr_max)

        return total_max  