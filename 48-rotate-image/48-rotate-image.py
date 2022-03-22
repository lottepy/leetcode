import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # # Method 1: Decomposite
        # def transpose(matrix):
        #     n = len(matrix)
        #     for i in range(n):
        #         for j in range(i+1, n):
        #             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # def flip(matrix):
        #     n = len(matrix)
        #     for j in range(n//2):
        #         for i in range(n):     
        #             matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]  

        # transpose(matrix)
        # flip(matrix)

        # Method 2: Direct replace              
        n = len(matrix)
        l, r = 0, n-1
        while l < r:
            for i in range(r-l):
                top, bot = l, r
                topLeft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bot-i][l]
                matrix[bot-i][l] = matrix[bot][r-i]
                matrix[bot][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topLeft
            l += 1
            r -= 1 