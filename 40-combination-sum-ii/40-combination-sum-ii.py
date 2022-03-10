class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Method 1: DP
        dp = [set() for _ in range(target)]

        for c in candidates:
            if c <= target:
                dp[c-1].add(tuple([c]))

        for i in range(target):
            if i >= min(candidates):
                for c in candidates:
                    if i-c >= 0 and len(dp[i-c]) > 0:
                        temp = []
                        for s in dp[i-c]:
                            if c in s:
                                _can = copy.deepcopy(candidates)
                                for p in s:
                                    _can.remove(p)
                                if c in _can:
                                    temp.append(tuple(sorted(list(s)+[c])))     
                            elif c not in s:
                                temp.append(tuple(sorted(list(s)+[c])))
                        dp[i] = set(temp).union(dp[i])

        return [list(t) for t in dp[-1]]