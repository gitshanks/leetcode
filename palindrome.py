https://leetcode.com/problems/palindrome-number/description/
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        sol = None
       
        #negative
        if(x<0):
            return False
        
        a = str(x)
        b = list(a)
        
        b.reverse()
        c = int(''.join(str(e) for e in b))
        
        
        if(x==c):
            sol = True
        else:
            sol = False
        
        return sol