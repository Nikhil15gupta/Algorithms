'''
Created on 27-Jun-2021

@author: nikhil
'''
def isBadVersion(version):
    pass

def firstBadVersion(n):
    left = 1
    right = n
    
    while left <= right:
        mid = (left + right)//2
        if isBadVersion(mid):
            if not(isBadVersion(mid-1)):
                return mid
            right = mid - 1
        else:
            left = mid + 1
