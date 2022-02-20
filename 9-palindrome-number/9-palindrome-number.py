import copy
class Solution:
    # # Method 1: revert
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False

    #     y = copy.deepcopy(x)
    #     _x = 0
    #     while x != 0:    
    #         _x = _x * 10 + x % 10
    #         x = x // 10
    #     if _x == y:
    #         return True    
    #     return False 

    # Method 2: revert half       
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False

        _x = 0
        while x > _x:    
            _x = _x * 10 + x % 10
            x = x // 10
        if x == _x // 10 or x == _x:
            return True    
        return False    