'''
Created on 25-Jun-2021

@author: nikhi
'''
def maxArea(height):
    left = 0
    right = len(height) - 1
    maxArea = 0
    
    while left < right:
        maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxArea

array = [2,3,4,5,18,17,6,1]
print(maxArea(array))