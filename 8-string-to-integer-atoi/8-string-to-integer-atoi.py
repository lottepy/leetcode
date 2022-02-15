MIN = -2147483648
MAX = 2147483647

class Solution:
    def myAtoi(self, s: str) -> int:
        def is_float(f):
            try:
                float(f)
                return True
            except:
                return False

        # Remove all spaces in front
        while len(s) > 0 and s[0] == ' ':
            s = s[1:]
        res = 0
        sign = 1
        signFlag = True if len(s) > 0 and is_float(s[0]) else False
        while len(s) > 0 and (is_float(s[0]) or (s[0] in ['+', '-']) and not signFlag):
            if  s[0] == '-':
                sign = -1
                s = s[1:]
                signFlag = True
                continue
            if s[0] == '+':
                s = s[1:]
                signFlag = True
                continue

            res = res * 10 + int(s[0])  
            s = s[1:]    

        s = res * sign
        if s <= MIN:
            return MIN
        elif s >= MAX:
            return MAX
        return s        
        
if __name__ == '__main__':
    print(Solution().myAtoi("   +0 123"))