'''
Created on 11-May-2021

@author: nikhi
'''
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes(nums):
    count = 0
    size = []
    mark = 0
    for i in nums:
        mark = i
        if i == 1:
            count+=1
    
        else:
            size.append(count)
            count = 0
    if mark == 1:
        size.append(count)
    return max(size)

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))