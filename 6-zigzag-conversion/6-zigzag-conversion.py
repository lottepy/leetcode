class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # # Method 1: Store in matrix
        # if numRows == 1:
        #     return s
        # dp = [[''] * (len(s) // (numRows - 1) + 1) for _ in range(numRows)]
        # count, i = 0, 0
        # while i < len(s):
        #     if count % numRows == 0 and i != 0:
        #         i -= 1
        #     else:    
        #         if count // numRows % 2 == 0:
        #             dp[count % numRows][count // numRows] = s[i]
        #         else:
        #             dp[numRows - count % numRows - 1][count // numRows] = s[i]        
        #     count += 1 
        #     i += 1
               
        # return ''.join([''.join(r) for r in dp])

        # Method 2: 
        if numRows == 1:
            return s

        res = ''
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if r % (numRows - 1) != 0 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]
        return res            


if __name__ == '__main__':
    s = "paypalishiring"
    sol = Solution()
    print(sol.convert(s, 2))         