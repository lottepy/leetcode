class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        l, r = intervals[0]
        res = []
        for subint in intervals[1:]:
            if r >= subint[0]:
                if r < subint[1]:
                    r = subint[1]
                if l > subint[0]:
                    l = subint[0]  
            else:
                res.append([l,r])
                l, r = subint    
        res.append([l,r])        
        return res