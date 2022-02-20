class Solution:
    # # Method 1: recursion
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if len(strs) == 0:
    #         return ''
        
    #     if len(strs[0]) != 0:
    #         ch = strs[0][0]
    #     else:
    #         return ''
    #     for i in range(1, len(strs)):
    #         if len(strs[i]) == 0 or strs[i][0] != ch:
    #             return ''
        
    #     return ch + self.longestCommonPrefix([s[1:] for s in strs])

    # Method 2: sorting
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        strs.sort()
        p = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y: 
                p+=x
            else: 
                break
        return p
