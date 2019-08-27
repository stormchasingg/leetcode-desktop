class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = -int(str(x)[::-1][:-1]) if x < 0 else int(str(x)[::-1])
        x = 0 if abs(x) > 0x7fffffff else x
        return x
    
