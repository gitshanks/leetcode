https://leetcode.com/problems/roman-to-integer/description/
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = list(s)
        flag = False
        
        s = 0
        
        for i in range(len(l)):
            if(flag==True):
                flag = False
                continue
            
            elif(l[i]=='I'):
                
                if(i+1<len(l) and l[i+1]=='V'):
                    s+=4
                    flag= True
                   
                elif(i+1<len(l) and l[i+1]=='X'):
                    s+=9
                    flag= True
                else:
                    s+=1
                    
                    
                    
            elif(l[i]=='V'):
                s+= 5
               
                
                
            elif(l[i]=='X'):
                
                if(i+1<len(l) and l[i+1]=='L'):
                    s+=40
                    flag= True
                    
                elif(i+1<len(l) and l[i+1]=='C'):
                    s+=90
                    flag= True
                else:
                    s+=10
                    
            
            

            elif(l[i]=='L'):
                s+=50
                
            
            
            elif(l[i]=='C'):
                
                if(i+1<len(l) and l[i+1]=='D'):
                    s+=400
                    flag= True
                    
                elif(i+1<len(l) and l[i+1]=='M'):
                    s+=900
                    flag= True
                else:
                    s+=100
                    
            
            
            elif(l[i]=='D'):
                s+=500
                
            
            elif(l[i]=='M'):
                s+=1000
            
        return s