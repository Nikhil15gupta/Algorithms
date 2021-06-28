'''
Created on 28-Jun-2021

@author: nikhil
'''
def singleNumber(nums):
    distinctNums = set(nums)
    return 2 * sum(distinctNums) - sum(nums)
  
print(singleNumber([1,2,2,3,1]))
            
        
        
        