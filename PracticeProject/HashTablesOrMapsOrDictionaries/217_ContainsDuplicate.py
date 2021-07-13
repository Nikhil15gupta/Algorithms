'''
Created on 12-Jul-2021

@author: nikhil
'''
# not a good method

# def containsDuplicate(nums):
#     lst = []
#     for i in nums:
#         if i in lst:
#             return True
#         lst.append(i)
#     return False  
#
# nums = [1,2,3,1]
# print(containsDuplicate(nums))

#------------ using set-----------------------------

def containsDuplicate(nums):
    unique = set(nums)
    if len(nums) == len(unique):
        return False
    return True

nums = [1,2,3,1]
print(containsDuplicate(nums))

#------------using map/dictionaries--------------
# def containsDuplicate(nums):
#     m = {}
#     for i in nums:
#         if i in m:
#             return True 
#         m[i] = 1
#     return False
# nums = [1,2,3,1]
# print(containsDuplicate(nums))
   