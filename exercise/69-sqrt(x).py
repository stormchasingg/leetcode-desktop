class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        t = x
        while t * t > x:
            t = (t + x / t) / 2
        return t
    
