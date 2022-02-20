class Solution:
    # # Method 1: recursion
    # def isMatch(self, s: str, p: str) -> bool:
    #     if not p:
    #         return not s    
    #     match = bool(s) and ((s[0] == p[0]) or (p[0] == '.'))
    #     if len(p) >= 2 and p[1] == '*':
    #         return (match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
    #     else:
    #         return match and self.isMatch(s[1:], p[1:])  

    # Method 2: iteration
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False    
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                return (match and dfs(i+1, j)) or dfs(i, j+2)
            if match:
                return dfs(i+1, j+1)    
            return False    
                  
        return dfs(0, 0)