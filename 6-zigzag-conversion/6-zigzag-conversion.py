class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        dp = [[''] * len(s) for _ in range(numRows)]
        count, i = 0, 0
        while i < len(s):
            if count % numRows == 0 and i != 0:
                i -= 1
            else:    
                if count // numRows % 2 == 0:
                    dp[count % numRows][count // numRows] = s[i]
                else:
                    dp[numRows - count % numRows - 1][count // numRows] = s[i]        
            count += 1 
            i += 1
               
        return ''.join([''.join(r) for r in dp])

if __name__ == '__main__':
    s = "AB"
    sol = Solution()
    print(sol.convert(s, 1))        