'''
Created on 29-Jun-2021

@author: nikhil
'''
def findRepeatedChars(s):
    chars = set()
    result = set()
    for i in s:
        if i in chars:
            result.add(i)
        else:
            chars.add(i)
    return result

print(findRepeatedChars("abcdefcgaba"))
