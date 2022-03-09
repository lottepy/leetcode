class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [set() for _ in range(target)]

        for c in candidates:
            if c <= target:
                dp[c-1].add(tuple([c]))

        for i in range(target):
            if i >= min(candidates):
                for c in candidates:
                    if i-c >= 0 and len(dp[i-c]) > 0:
                        temp = set([tuple(sorted(list(s) + [c])) for s in dp[i-c]])
                        dp[i] = temp.union(dp[i])

        return [list(t) for t in dp[-1]]  
if __name__ == '__main__':
    print(Solution().combinationSum([2,3,6,7],7))