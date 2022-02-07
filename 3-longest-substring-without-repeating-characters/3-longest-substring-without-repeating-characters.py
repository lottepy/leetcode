from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash= defaultdict(lambda: 0)
        left = 0
        ans = 0

        for right in range(len(s)):
            while hash[s[right]] != 0:
                hash[s[left]] = hash.get(s[left], 1) - 1
                left += 1
            hash[s[right]] += 1
            ans = max(ans, right - left + 1)
        return ans    

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))