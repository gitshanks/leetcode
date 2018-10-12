https://leetcode.com/problems/reverse-integer/description/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x<0):
            z = -1*x
        else:
            z = x
        a = str(z)
        b = list(a)
        b.reverse()
        c = int(''.join(str(e) for e in b))
        
        if(c>(2**31) or c<(-2**31)):
            return 0
        
        if(x<0):
            return -1 * c
        else:
            return c