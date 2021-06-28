'''
Created on 28-Jun-2021

@author: nikhil
'''
def missingNumber(nums):
    currentSum = sum(nums)
    n = len(nums)
    intendedSum = n*(n+1)/2
    return int(intendedSum - currentSum)

print(missingNumber([3,0,1]))