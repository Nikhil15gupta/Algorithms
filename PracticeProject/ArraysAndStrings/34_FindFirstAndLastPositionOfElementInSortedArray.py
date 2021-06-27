'''
Created on 27-Jun-2021

@author: nikhil
'''
def getLeftPosition(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            if (mid == 0) or (nums[mid-1] != target):
                return mid
            right = mid -1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
   
def getRightPosition(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            if (mid == len(nums) - 1) or (nums[mid+1] != target):
                return mid
            left = left + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1            
    return -1

def searchRange(nums, target):
    left = getLeftPosition(nums, target)
    right = getRightPosition(nums, target)
    return [left,right]
                
nums = []
target = 0
print(searchRange(nums, target))
    