'''
Created on 28-Jun-2021

@author: nikhil
'''
from math import sqrt, ceil
def countPrimes(n):
    if n < 2:
        return 0
    
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    
    for i in range(2, ceil(sqrt(n))):    
        if isPrime[i]:
            for multiples_of_i in range(i*i,n,i):
                isPrime[multiples_of_i] = False
    return sum(isPrime)
        
print(countPrimes(9))