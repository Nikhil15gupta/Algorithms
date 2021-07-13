'''
Created on 12-Jul-2021

@author: nikhil
'''
# def twoSum(nums, target):
#     length = len(nums)
#     result = []
#     for i in range(length):
#         for j in range(i + 1, length):
#             if nums[i] + nums[j] == target:
#                 result.append(i)
#                 result.append(j)
#                 return result
#
# print(twoSum([3,3], 6))

# Using Dictionaries/Maps

def twoSum(nums, target):
    m = {}
    for i in range(len(nums)):
        goal = target - nums[i]
        if goal in m:
            return [m[goal], i]
        m[nums[i]] = i 

print(twoSum([3,3], 6))
