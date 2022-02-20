class Solution:
    # Method 1: Brute Force
    def intToRoman(self, num: int) -> str:
        romanMap = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        invRomanMap = {v: k for k, v in romanMap.items()}
        subtractionMap = {'V': 'I', 'X': 'I', 'L': 'X', 'C': 'X', 'D': 'C', 'M': 'C'}
        elements = list(romanMap.keys())
        elements.sort()
        res = ''
        pos = len(elements) - 1
        while num != 0 and pos >= 0:
            residual = num % elements[pos]
            multi = num // elements[pos]
            # if residual > 10:
            subtraction = (multi == 0 and elements[pos] - residual <= invRomanMap[subtractionMap[romanMap[elements[pos]]]])
            # else:
            #     subtraction = ((pos == 2 and residual == 9) or (pos == 1 and residual == 4))    
            if multi != 0 or subtraction:
                if multi != 0:
                    res += romanMap[elements[pos]] * multi    
                    num = num % elements[pos]
                elif subtraction:
                    res += subtractionMap[romanMap[elements[pos]]] + romanMap[elements[pos]]
                    num = num % invRomanMap[subtractionMap[romanMap[elements[pos]]]]
            else:
                pos -= 1    
        return res
        
if __name__ == '__main__':
    print(Solution().intToRoman(8))