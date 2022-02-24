class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        axcii = [ord(d) for d in digits if d not in ['1', '*', '0', '#']]
        res = []
        for a in axcii:
            if a < 55:
                _chr = [chr(96 + (a-50)*3 + i) for i in range(1,4)]
            elif a == 55:
                _chr = [chr(96 + (a-50)*3 + i) for i in range(1,5)]
            elif a == 56:        
                _chr = [chr(96 + (a-51)*3 + 4 + i) for i in range(1,4)]
            else:
                _chr = [chr(96 + (a-51)*3 + 4 + i) for i in range(1,5)] 
            if len(res) == 0:
                res = _chr
            else:
                res = [r + c for r in res for c in _chr]
        return res

if __name__ == '__main__':
    print(Solution().letterCombinations('123'))