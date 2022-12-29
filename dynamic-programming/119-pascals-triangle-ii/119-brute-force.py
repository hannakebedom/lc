class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
        solution type: brute-force
        time complexity: O(n^2)
        description: use the same approach as pascal's triangle, return last row
            - a more efficient solution would use the binomial coefficent formula
        '''
        rowIndex += 1
        res = [[1]]
        for i in range(1, rowIndex):
            row = [1]
            for j in range(1, i):
                row.append(res[i - 1][j - 1] + res[i - 1][j])
            row.append(1)
            res.append(row)
        return res[-1]