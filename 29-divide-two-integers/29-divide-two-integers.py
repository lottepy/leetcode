class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN = - 2147483648
        MAX = 2147483647
        def pos(num1, num2):
            if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
                return True
            else:
                return False    
        def cap(num, sign):
            if -num < MIN and not sign:
                return -MIN
            elif num > MAX and sign:
                return MAX
            else:
                return num 


        count = 0
        sign = pos(dividend, divisor)
        dividend, divisor = abs(dividend), abs(divisor)
        
        for i in range(31, -1, -1):
            if divisor << i <= dividend:
                dividend -= divisor << i
                count += 1 << i
        count = cap(count, sign)    
        return count if sign else -count   
