class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        l, r = 1, x
        while l <= r:
            m = l + (r - l) // 2
            sq = m * m
            sqNext = sq + 2*m + 1
            if sq <= x and x < sqNext:
                return m
            elif sq > x:
                r = m - 1
            else:
                l = m + 1
        return m 