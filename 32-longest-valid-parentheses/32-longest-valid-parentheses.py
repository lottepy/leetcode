class Solution:
    def longestValidParentheses(self, s: str, memo = dict()) -> int: 
        # Method 1: recursion
        # if len(s) == 1:
        #     return 0
        # elif s == '()':
        #     return 2
        # elif len(s) == 2 and s != '()':
        #     return 0           
        # elif len(s) % 2 == 1:
        #     return max(self.longestValidParentheses(s[:-1]), 
        #     self.longestValidParentheses(s[1:]))  
        # stack = []
        # for i in range(len(s)):
        #     if len(stack) > 0 and stack[-1] + s[i] == '()':
        #         stack.pop(-1)
        #     else:
        #         stack.append(s[i])

        # if len(stack) == 0:
        #     return len(s)
        # else:
        #     return max(self.longestValidParentheses(s[:-1]), 
        #                 self.longestValidParentheses(s[1:]))         

        # # Method 1.1: recursion with memo
        # if s in memo:
        #     return memo[s]
        # if len(s) == 1:
        #     memo[s] = 0
        #     return 0
        # elif s == '()':
        #     memo[s] = 2
        #     return 2
        # elif len(s) == 2 and s != '()':
        #     memo[s] = 0
        #     return 0    
        # elif len(s) % 2 == 1:
        #     return max(self.longestValidParentheses(s[:-1], memo), 
        #     self.longestValidParentheses(s[1:], memo))      

        # stack = []
        # for i in range(len(s)):
        #     if len(stack) > 0 and stack[-1] + s[i] == '()':
        #         stack.pop(-1)
        #     else:
        #         stack.append(s[i])

        # if len(stack) == 0:
        #     memo[s] = len(s)
        #     return memo[s]
        # else:
        #     return max(self.longestValidParentheses(s[:-1], memo), 
        #                 self.longestValidParentheses(s[1:], memo))     

        # # Method 2: DP Tabulation 2D
        # if len(s) == 0:
        #     return 0
        # dp = [[0] * len(s) for _ in range(len(s))]

        # res = 0
        # for i in range(1, len(s)):
        #     if s[i-1:i+1] == '()':
        #         dp[i-1][i] = 2
        #         res = max(res, 2)
        
        # for l in range(4, len(s)+1, 2):     
        #     for i in range(l-1, len(s)):
        #         if dp[i-l+2][i-1] != 0:
        #             if s[i-l+1] == '(' and s[i] == ')':
        #                 dp[i-l+1][i] = l
        #                 res = max(res, l)
        #         if sum(dp[i-l+1][:]) != 0 or sum(dp[:][i]) != 0:
        #             for k in range(2, l // 2 + 1, 2):
        #                 temp = dp[i-l+1][i-k]
        #                 if temp != 0:
        #                     rest = l - temp
        #                     if dp[i-rest+1][i] != 0:
        #                         dp[i-l+1][i] = l       
        #                         res = max(res, l)
        #                         break
        #                 temp = dp[i-l+k+1][i]        
        #                 if temp != 0:
        #                     rest = l - temp
        #                     if dp[i-l+1][i-l+rest] != 0:
        #                         dp[i-l+1][i] = l       
        #                         res = max(res, l)
        #                         break
                
        # return res

        # Method 2.2: DP Tabulation 1D
        if len(s) == 0:
            return 0
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i-1:i+1] == '()':
                dp[i] = dp[i-2] + 2
            elif dp[i-1] != 0:
                if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] + s[i] == '()':
                    temp = dp[i-1] + 2
                    dp[i] = temp + dp[i-temp]

        return max(dp)              


        # # Method 3: Stack
        # if len(s) == 0:
        #     return 0
        # stack = [-1]
        # res = 0
        # for i in range(len(s)):
        #     if i == 0:
        #         stack.append(0)
        #     elif len(stack) > 1 and s[stack[-1]] + s[i] == '()':
        #         stack.pop() 
        #         res = max(res, i - stack[-1])
        #     else:
        #         stack.append(i)    
        # return res


if __name__ == '__main__':
    print(Solution().longestValidParentheses("(())()(())"))


if __name__ == '__main__':
    print(Solution().longestValidParentheses(")(((((()())()()))()(()))("))