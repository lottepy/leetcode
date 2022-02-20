class Solution:
    # # Method 1: recursion
    # def isMatch(self, s: str, p: str, memo = dict()) -> bool:
    #     if not p:
    #         memo[(s, p)] = not s
    #         return memo[(s, p)]   
    #     match = bool(s) and ((s[0] == p[0]) or (p[0] == '.'))
    #     if len(p) >= 2 and p[1] == '*':
    #         memo[(s,p)] = (match and self.isMatch(s[1:], p, memo)) or self.isMatch(s, p[2:], memo)
    #         return memo[(s,p)]
        
    #     memo[(s,p)] = match and self.isMatch(s[1:], p[1:], memo)  
    #     return memo[(s,p)]

    # Method 2: iteration
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(s) and j >= len(p):
                memo[(i, j)] = True
                return True
            if j >= len(p):
                memo[(i, j)] = False
                return False    
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                memo[(i, j)] = (match and dfs(i+1, j)) or dfs(i, j+2)
                return memo[(i, j)]

            memo[(i, j)] = match and dfs(i+1, j+1)    
            return memo[(i, j)]    
                  
        return dfs(0, 0)