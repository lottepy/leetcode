class Solution:
    # # Method 1: Recursion
    # def longestPalindrome(self, s: str) -> str:
    #     if s == s[::-1]:
    #         return s
    #     else:
    #         lower = self.longestPalindrome(s[:-1])
    #         upper = self.longestPalindrome(s[1:])
    #         return lower if len(lower) > len(upper) else upper
     
    # Method 2: Tabeulation
    def longestPalindrome(self, s: str) -> str:
        def palindrome(left, right):
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]    

        res = s[0]
        for l in range(len(s) - 1):
            odd = palindrome(l, l)
            even = palindrome(l, l+1)
            if max(len(odd), len(even)) > len(res):
                res = odd if len(odd) > len(even) else even
        return res        


if __name__ == '__main__':
    s = 'abbca'
    sol = Solution()
    print(sol.longestPalindrome(s))           