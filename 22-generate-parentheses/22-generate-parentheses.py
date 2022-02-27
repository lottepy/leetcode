class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return []
        elif n == 1:
            return ['()']    
        stack = []
        res = []
        def backtracking(open, close):
            if open == close == n:
                res.append(''.join(stack))
                return None
            if open < n:
                stack.append('(')
                backtracking(open+1, close)
                stack.pop()
            if close < open:
                stack.append(')')
                backtracking(open, close+1)
                stack.pop()
        backtracking(0, 0)
        return res        

if __name__ == '__main__':
    print(Solution().generateParenthesis(4))