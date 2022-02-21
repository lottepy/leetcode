
# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        romanMap = {v: k for k, v in romanMap.items()}
        elements = list(romanMap.keys())
        res = 0
        pos = len(elements) - 1
        while len(s) > 0 and pos >= 0:
            roman = elements[pos]
            if (len(roman) == 1 and roman == s[0]) or (len(roman) == 2 and len(s) >= 2 and roman == s[:2]):
                res += romanMap[roman]
                s = s[len(roman):]
            else:
                pos -= 1
        return res            
if __name__ == '__main__':
    print(Solution().romanToInt('MCMXCIV'))