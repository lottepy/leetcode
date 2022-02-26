
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']': '[', '}': '{', ')': '('}
        res = []
        for chr in s:
            if len(res) > 0 and chr in pairs.keys() and res[-1] == pairs[chr]:
                res = res[:-1]    
            elif len(res) == 0 or res[-1] not in pairs.keys():
                res.append(chr)   
            else:
                return False
        return len(res) == 0            

if __name__ == '__main__':
    print(Solution().isValid("{[]}"))