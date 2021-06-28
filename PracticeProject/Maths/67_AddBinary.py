'''
Created on 28-Jun-2021

@author: nikhil
'''
def addBinary(a, b):
    i,j = len(a)-1, len(b)-1
    result = []
    carry = 0
    while i>=0 or j>=0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
            
        result.append(str(total % 2))
        carry = total//2
        
        
    return ''.join(reversed(result))

print(addBinary("1010", "1011"))
