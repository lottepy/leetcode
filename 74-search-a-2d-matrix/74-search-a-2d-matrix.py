class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i = 0
        prev = matrix[i][0]
        if target < prev:
            return False
        for i in range(1,m):
            curr = matrix[i][0]
            if target >= prev and target < curr:
                i = i -1
                break
            if i == m-1 and target >= curr:
                break
            prev = curr
        try:
            return matrix[max(0, i)].index(target) >= 0
        except Exception as ex:
            return False