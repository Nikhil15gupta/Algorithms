'''
Created on 25-Jun-2021

@author: nikhi
'''
array = [0,1,0,3,12]

def moveZeroes(arr):
    n = len(arr)
    j = 0
    for num in arr:
        if num != 0:
            arr[j] = num
            j += 1
    for i in range(j,n):
        arr[i]=0       
        
    print(arr)
moveZeroes(array)
            