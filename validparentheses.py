https://leetcode.com/problems/valid-parentheses/description/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = True
        l = list(s)
        bl = []   #stack
        
        for p in l:
            if(p =='(' or p =='{' or p =='['):
                bl.append(p) #push
            
            else:                   #pop
                if(len(bl) ==0):    #no element in stack
                    return False
                
                if(p==')' and bl[-1] == '('):
                    flag = True
                    del bl[-1]
                elif(p=='}' and bl[-1] == '{'):
                    flag = True
                    del bl[-1]
                elif(p==']' and bl[-1] == '['):
                    flag = True
                    del bl[-1]
                
                else:               #if bracket never opened
                    flag = False
                    return flag
        
        #if there is still a bracket left unclosed
        if(len(bl)>0):
            return False
        
        return flag