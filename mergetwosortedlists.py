https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lt1=[]
        lt2=[]
        
        if(l1!= None):
            self.lt(l1,lt1)
        
        if(l2!= None):   
            self.lt(l2,lt2)
        
        return sorted(lt1 + lt2)
    
    def lt(self, llink,l):
        if(llink.next == None):
            l.append(llink.val)
        else:
            self.lt(llink.next,l)
            l.append(llink.val)
        return l