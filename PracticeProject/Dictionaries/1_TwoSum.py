'''
Created on 12-Jul-2021

@author: nikhil
'''
nums = [3, 3]
target = 6

# Brute Force
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#
# print(twoSum(nums, target))
# Time complexity: O(n^2)

# Using Dictionary
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        goal = target - nums[i]
        if goal in d:
            return [d[goal], i]
        d[nums[i]] = i 

print(twoSum(nums, target))
# Time complexity: O(n)
