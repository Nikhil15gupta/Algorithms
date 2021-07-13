'''
Created on 12-Jul-2021

@author: nikhil
'''
# def majorityElement(nums):
#     m = {}
#     length = len(nums)
#     for i in nums:
#         if i in m:
#             m[i] += 1
#         else:
#             m[i] = 1
#         if m[i] > length/2:
#                 return i

def majorityElement(nums):
    m = {}
    length = len(nums)
    for i in nums:
        m[i] = m.get(i,0) + 1
        if m[i] > length/2:
                return i
nums = [2,2,2]
print(majorityElement(nums))