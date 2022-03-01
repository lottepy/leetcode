class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        for i in range(0, len(haystack) - len(needle) + 1):
            if needle == haystack[i:i+len(needle)]:
                return i    
                
        return -1        