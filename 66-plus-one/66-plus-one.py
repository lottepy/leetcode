class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return digits

        incre = 1
        for i in range(len(digits)-1, -1, -1):
            temp = digits[i]
            digits[i] = (temp + incre) % 10
            incre = (temp + incre) // 10

        if incre > 0:
            digits = [incre] + digits

        return digits           