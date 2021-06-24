'''
Created on 28-Apr-2021

@author: nikhi
'''
# Given an integer n, return true if it is a power of three. Otherwise, 
# return false.
#
# An integer n is a power of three, if there exists an integer x such that
#  n == 3x.
# 
from math import log

def isPowerOfThree(n):
    if n<3:
        return False
    ans = log(n,3)
    return abs(round(ans)-ans)<1e-10
       

n = 45
print(isPowerOfThree(n))

#Explanation: https://dev.to/seanpgallivan/solution-power-of-three-1g6g#idea

