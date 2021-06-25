'''
Created on 25-Jun-2021

@author: nikhi
'''
array = [1,3,2,2]
limit = 3

def numRescueBoats(arr, limit):
    arr.sort()
    
    left = 0
    right = len(arr)-1
    boatsNumber = 0
    
    while left <= right :
        if left == right :
            boatsNumber += 1
            break
        if arr[left] + arr[right] <= limit:
            boatsNumber += 1
            left += 1
            right -= 1
        else:
            boatsNumber += 1
            right -= 1
    return boatsNumber

print(numRescueBoats(array, limit))
            
            