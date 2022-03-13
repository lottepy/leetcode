class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = False
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ' and flag == False:
                continue
            elif s[i] != ' ' and flag == False:
                flag = True
                count += 1
            elif s[i] != ' ' and flag == True:
                count += 1
            elif s[i] == ' ' and flag == True:
                return count
        return count    