class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        solution type: optimal
        time complexity: O(n^2)
        description: start with 1 and build up the solution using the previous computed results 
        '''
        res = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(res[i - 1][j - 1] + res[i - 1][j])
            row.append(1)
            res.append(row)
        return res