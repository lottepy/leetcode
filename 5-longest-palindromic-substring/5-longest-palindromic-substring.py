class Solution:
    # Method 1: DP Tabulation
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i < len(s) - 1:
                if s[i+1] == s[i]:
                    dp[i][i+1] = True
                    res = s[i:i+2] if len(s[i:i+2]) > len(res) else res

        for l in range(2,len(s)):
            for i in range(len(s)-l):
                j = i + l
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    res = s[i:j+1] if len(s[i:j+1]) > len(res) else res
        return res


    # # Method 2: Expansion
    # def longestPalindrome(self, s: str) -> str:
    #     def palindrome(substr):
    #         if len(substr) < 2:
    #             return True
    #         if substr[0] != substr[-1]:
    #             return False
    #         return palindrome(substr[1:-1])    

    #     res = s[0]
    #     for l in range(len(s) - 1):
    #         odd = palindrome(l, l)
    #         even = palindrome(l, l+1)
    #         if max(len(odd), len(even)) > len(res):
    #             res = odd if len(odd) > len(even) else even
    #     return res        


if __name__ == '__main__':
    s = 'cbbd'
    sol = Solution()
    print(sol.longestPalindrome(s))        