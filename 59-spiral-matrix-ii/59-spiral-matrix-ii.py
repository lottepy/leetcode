import numpy as np
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        elif n == 2:
            return [[1,2],[4,3]] 

        inner = (np.array(self.generateMatrix(n-2)) + n**2 - (n-2)**2).tolist()
        res = [list(range(1, n+1))]
        for i in range(n-2):
            res.append([inner[0][0]-i-1] + inner[i] + [n+1+i])
        res.append(list(range(2*n-1, inner[0][0]-n+2))[::-1])    
        return res