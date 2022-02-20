class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        if len(strs[0]) != 0:
            ch = strs[0][0]
        else:
            return ''
        for i in range(1, len(strs)):
            if len(strs[i]) == 0 or strs[i][0] != ch:
                return ''
        
        return ch + self.longestCommonPrefix([s[1:] for s in strs])