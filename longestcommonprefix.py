https://leetcode.com/problems/longest-common-prefix/description/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        info=[]
        flag = True
        c=1
        
        for i in strs:
            i = list(i)
            info.append(i)
        
        pre =''
        
        if(len(info)==0):
            return pre
        
        for i in range(len(info[0])):
            cmp = info[0][i]
            
            #if any match fails
            if(flag==False):
                break
            
            else:
                
                for j in range(1,len(info)):
                    
                    #for empty strings
                    if(len(info[j])==0):
                        return ""
                    
                    #for index out of range cases
                    if(len(info[j])>i):
                        
                        #if match is found
                        if(info[j][i]==cmp):
                            c+=1   
                        else:
                            flag = False  
                            break
                
                #if the character is in every string
                if(c==len(info)):
                    pre+=cmp
                    c=1
                
        return pre