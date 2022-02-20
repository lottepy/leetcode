import copy
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        y = copy.deepcopy(x)
        _x = 0
        while x != 0:    
            _x = _x * 10 + x % 10
            x = x // 10
        if _x == y:
            return True    
        return False    
