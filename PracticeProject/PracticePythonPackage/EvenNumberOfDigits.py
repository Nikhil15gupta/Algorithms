'''
Created on 11-May-2021

@author: nikhi
'''
# Given an array nums of integers, return how many of them contain an even number of digits.

def findNumbers(nums):
    count = 0
    for i in nums:
        if numOfDigits(i)%2==0:
            count+=1
    return count

def numOfDigits(num):
    count = 0
    while num>0:
        num//=10
        count+=1
    return count

print(findNumbers([555,901,482,1771]))