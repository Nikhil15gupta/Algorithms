'''
Created on 10-May-2021

@author: nikhil
'''
# Given an array of integers target. From a starting array, A consisting of 
# all 1's, you may perform the following procedure :
#
# let x be the sum of all elements currently in your array.
# choose index i, such that 0 <= i < target.size and set the value of A at 
# index i to x.
# You may repeat this procedure as many times as needed.
# Return True if it is possible to construct the target array from A otherwise 
# return False.
from heapq import heapify,heappop, heappush
def isPossible(target):
        heap = [-num for num in target]
        total = sum(target)
        heapify(heap)
        while heap[0] != -1:
            num = -heappop(heap)
            total -= num
            if num <= total or total < 1: return False
            num %= total
            total += num
            heappush(heap, -num)
        return True
    
print(isPossible([5,3,9]))

# Explanation: https://dev.to/seanpgallivan/solution-construct-target-array-with-multiple-sums-24d4
    