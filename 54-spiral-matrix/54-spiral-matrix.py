import numpy as np
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrix = np.array(matrix)
        l, r = 0, len(matrix[0])-1
        top, bottom = 0, len(matrix)-1
        res = []
        while l <= r and top <= bottom:
            res += matrix[top, l:r+1].tolist()
            res += matrix[top+1:bottom+1, r].tolist()
            if bottom > top:
                res += matrix[bottom,l:r][::-1].tolist()
            if r > l:    
                res += matrix[top+1:bottom,l][::-1].tolist()
            l += 1
            r -= 1
            top += 1
            bottom -= 1
        return res    
        