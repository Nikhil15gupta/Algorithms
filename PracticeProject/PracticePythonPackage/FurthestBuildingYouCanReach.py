'''
Created on 27-Apr-2021

@author: nikhi
'''
from heapq import heappush, heappop
heights = [2,7,9,12]
bricks = 5
ladders = 1

def furthestBuilding(heights, bricks, ladders):
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if ladders > 0:
                    heappush(heap, diff)
                    ladders -= 1
                elif heap and diff > heap[0]:
                    heappush(heap, diff)
                    bricks -= heappop(heap)
                else: bricks -= diff
                if bricks < 0: return i
        return len(heights) - 1
    
print(furthestBuilding(heights, bricks, ladders))
#
#
#
# print(furthestBuilding(heights, bricks, ladders))

# Explanation: https://dev.to/seanpgallivan/solution-furthest-building-you-can-reach-1m24#idea
# using heappop(heap), always smallest value will be popped which is at heap[0]