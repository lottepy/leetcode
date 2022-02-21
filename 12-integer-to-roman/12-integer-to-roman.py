class Solution:
    # # Method 1: Brute Force
    # def intToRoman(self, num: int) -> str:
    #     romanMap = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    #     invRomanMap = {v: k for k, v in romanMap.items()}
    #     subtractionMap = {'V': 'I', 'X': 'I', 'L': 'X', 'C': 'X', 'D': 'C', 'M': 'C'}
    #     elements = list(romanMap.keys())
    #     elements.sort()
    #     res = ''
    #     pos = len(elements) - 1
    #     while num != 0 and pos >= 0:
    #         residual = num % elements[pos]
    #         multi = num // elements[pos]
    #         subtraction = (multi == 0 and elements[pos] - residual <= invRomanMap[subtractionMap[romanMap[elements[pos]]]])  
    #         if multi != 0 or subtraction:
    #             if multi != 0:
    #                 res += romanMap[elements[pos]] * multi    
    #                 num = residual
    #             elif subtraction:
    #                 res += subtractionMap[romanMap[elements[pos]]] + romanMap[elements[pos]]
    #                 num = num % invRomanMap[subtractionMap[romanMap[elements[pos]]]]
    #         else:
    #             pos -= 1    
    #     return res

    # Method 2: Construct mapping
    def intToRoman(self, num: int) -> str:
        romanMap = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        elements = list(romanMap.keys())
        elements.sort()
        res = ''
        pos = len(elements) - 1

        while num != 0 and pos >= 0:
            residual = num % elements[pos]
            multi = num // elements[pos]
            if multi != 0:
                res += romanMap[elements[pos]] * multi  
                num = residual
            else:
                pos -= 1
        return res