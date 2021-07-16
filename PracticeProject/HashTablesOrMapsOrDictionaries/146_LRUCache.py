'''
Created on 16-Jul-2021

@author: nikhil
'''
from _collections import deque
def __init__(self, capacity):
    self.c = capacity
    self.m = {}
    self.deq = deque()
         
def get(self, key):
    if key not in self.m:
        return -1
    else:
        self.deq.remove(key)
        self.deq.append(key)
        return self.m[key]
    
    
def put(self, key, value):
    if key not in self.m:
        if len(self.deq) == self.c:
            oldest = self.deq.popleft()
            del self.m[oldest]
    else:
        self.deq.remove(key)
    self.m[key] = value
    self.deq.append(key)
    
            
            
            
            