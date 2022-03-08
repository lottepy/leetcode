class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        res = ''
        prev = self.countAndSay(n-1)
        for i in range(len(prev)):
            if i == 0:
                count = 1
            elif i > 0 and prev[i] != prev[i-1]:
                res += f'{count}{prev[i-1]}'
                count = 1
            else:
                count += 1   
        res += f'{count}{prev[i]}'         
        return res
