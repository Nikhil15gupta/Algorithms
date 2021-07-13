'''
Created on 12-Jul-2021

@author: nikhil
'''
def groupAnagrams(strs):
    hashMap = {}
    answer = []
    for i in strs:
        sortedString = ''.join(sorted(i))
        if sortedString not in hashMap:
            hashMap[sortedString] = []
        hashMap[sortedString].append(i)
    for i in hashMap.values():
        answer.append(i)
    return answer
        
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))       