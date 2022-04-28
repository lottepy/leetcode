class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]

        res = self.generate(numRows-1)
        new = [res[-1][0]]
        for i in range(len(res[-1])-1):
            new.append(res[-1][i] + res[-1][i+1])
        new.append(res[-1][-1])    
        res.append(new)
        return res