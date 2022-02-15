import math

MIN = -2147483648
MAX = 2147483647

class Solution:
    # # Method 1: Brute Force
    # def reverse(self, x: int) -> int:
    #     if x == 0 or math.log2(abs(x)) > 31:
    #         return 0
    #     sign = -1 if x < 0 else 1
    #     x = abs(x)
    #     res, i = 0, 0
    #     n = int(math.log10(x))
    #     while x != 0:
    #         res += (x % 10) * (10 ** (n - i))
    #         x = x // 10
    #         i += 1
    #     return res * sign if math.log2(res) <= 31 else 0

    # Method 2: solve overflow
    def reverse(self, x: int) -> int:
        res = 0
        while x != 0:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if (res > MAX // 10) or ((res == MAX // 10) and (digit > MAX % 10)):
                return 0
            if (res < int(MIN / 10)) or ((res == int(MIN / 10)) and (digit < math.fmod(MIN, 10))):
                return 0
            res = res * 10 + digit
            
        return res
        
if __name__ == '__main__':
    print(Solution().reverse(-1563847412))