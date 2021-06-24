'''
Created on 09-May-2021

@author: nikhi
'''

# Let's say a positive integer is a super-palindrome if it is a palindrome, 
# and it is also the square of a palindrome.
#
# Given two positive integers left and right represented as strings, 
# return the number of super-palindromes integers in the inclusive 
# range [left, right].
from math import sqrt

def superpalindromesInRange(left,right):
    count = 1 if int(left)<=9 and int(right)>=9 else 0
    for i in range(1,19684):
        b3 = base3(i,"")
        if isPalindrome(b3):
            square = int(int(b3)*int(b3))
            if square > int(right):
                return count  
            if square >= int(left) and isPalindrome(str(square)):
                # print(int(b3)*int(b3))
                count += 1
    return count


def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False

def base3(n, num):
            if not n: 
                return num
            n, r = divmod(n, 3)
            return base3(n, str(r) + num)
        

print(superpalindromesInRange(4,1000))

#Explanation: https://dev.to/seanpgallivan/solution-super-palindromes-30d
