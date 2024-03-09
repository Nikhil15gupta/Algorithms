'''
Created on 27-Jun-2021

@author: nikhil
'''
def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        left = 0
        right = 0
        n = len(s)
        ans = 0 
        while left < n and right < n:
            el = s[right]
            if el in m:
                left = max(left, m[el] + 1)
            m[el] = right
            ans = max(ans, right - left + 1)
            right += 1
        return ans
    
string = "abcabcbb"
print(lengthOfLongestSubstring(string))
        
            