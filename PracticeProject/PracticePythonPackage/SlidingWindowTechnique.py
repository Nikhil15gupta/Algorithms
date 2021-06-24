'''
Created on 24-Jun-2021

@author: nikhi
'''
# Given an array(or list in python), find the maximum sum of k consecutive numbers in the array

array = [80, -50, 90, 100]
k = 2

# Brute Force Algorithm

def maxSum1(arr, k):
    maxSum = -100000
    arraySize = len(arr)
    for i in range(arraySize - k + 1):
        currSum = 0
        for j in range(k):
            currSum += arr[i+j]
        maxSum = max(maxSum, currSum)
    return maxSum

print(maxSum1(array, k))

# Sliding Window technique

def maxSum(arr, windowSize):
    windowSum = sum([arr[i] for i in range(windowSize)])
    maxSum = windowSum
    arraySize = len(arr)
    for i in range(arraySize - windowSize):
        windowSum = windowSum - arr[i] + arr[i+windowSize]
        maxSum = max(maxSum, windowSum)
    return maxSum

print(maxSum(array, k))
        

        
    

        
    

