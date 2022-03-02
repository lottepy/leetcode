import copy
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        wordNum = len(words)
        count = 0
        res = []
        for i in range(0, len(s)-wordLen*wordNum+1):
            _words = copy.deepcopy(words)
            flag = True
            while flag:
                temp = s[i:i+wordLen]
                if temp in _words and count < wordNum:
                    _words.remove(temp)
                    count += 1
                else:
                    if len(_words) == 0:
                        res.append(i-wordLen*count)
                    flag = False
                    count = 0
                i += wordLen    
        return res   