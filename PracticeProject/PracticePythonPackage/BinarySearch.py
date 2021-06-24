'''
Created on 24-Jun-2021

@author: nikhi
'''
def binarySearch(lst, target):
    left = 0
    right = len(lst)-1
    
    while left<=right:
        mid = (left+right)//2
        if target == lst[mid]:
            return mid
        elif target > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

lst = [1,2,3,4,5,6]
target = 4

result = binarySearch(lst, target)

if result != -1:
    print("Element is present at index %d"%result)
else:
    print("Element is not present in the list")