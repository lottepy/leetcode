import math
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or math.log2(abs(x)) > 31:
            return 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        res, i = 0, 0
        n = int(math.log10(x))
        while x != 0:
            res += (x % 10) * (10 ** (n - i))
            x = x // 10
            i += 1
        return res * sign if math.log2(res) <= 31 else 0
    
if __name__ == '__main__':
    print(Solution().reverse(1534236469))