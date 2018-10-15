https://leetcode.com/problems/add-two-numbers/description/
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = ''
        s2 = ''
        
        flag = True
        
        #traversing linked list
        while(l1 != None):
            s1+=str(l1.val)
            l1 = l1.next
        #traversing linked list   
        while(l2!= None):
            s2+=str(l2.val)
            l2 = l2.next
            
        #getting the actual numbers
        s1 = s1[::-1]
        s2 = s2[::-1]
        
        #sum
        x = int(s1) + int(s2)
        y = list(str(x))
    
        #converting characters to digits
        z=[]
        for i in y:
            z.append(int(i))
        
        #returning in reverse order
        z.reverse()
        
        return z