class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        hash = collections.defaultdict(list)
        for i in range(len(strs)):
            elements = tuple(sorted(list(strs[i])))
            hash[elements].append(strs[i])
        return list(hash.values())    