'''
Created on 17-Jul-2021

@author: nikhil
'''
def minWindow(s, t):
   len1 = len(s)
   len2 = len(t)
   
   if len1 < len2:
       return ""
   
   hashPat = {}
   hashStr = {}
   
   for i in t:
       hashPat[i] = hashPat.get(i, 0) + 1
        
   count = 0
   left = 0
   startIndex = -1
   minLen = float("inf")
   
   for right in range(0, len1):
       hashStr[s[right]] = hashStr.get(s[right], 0) + 1
       
       if hashStr[s[right]] <= hashPat.get(s[right],0):
           count += 1
       if(count == len2):
           while hashStr.get(s[left]) > hashPat.get(s[left], 0):
               hashStr[s[left]] -= 1
               left += 1
           windowLen = right - left + 1
           if(minLen > windowLen):
               minLen = windowLen
               startIndex = left
   if startIndex == -1:
        return ""
   return s[startIndex: startIndex + minLen]
    
s = "ADOBECODEBANC"
t = "ABC"      
print(minWindow(s, t))         
        