'''
Created on 12-Jul-2021

@author: nikhil
'''
def fourSumCount(nums1, nums2, nums3, nums4):
    m = {}
    ans = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            sums = nums1[i] + nums2[j]
            m[sums] = m.get(sums, 0) + 1
    for k in range(len(nums3)):
        for l in range(len(nums4)):
            target = -(nums3[k] + nums4[l])
            ans += m.get(target, 0)
    return ans
nums1 = [1,2]
nums2 = [0]
nums3 = [0]
nums4 = [0]
print(fourSumCount(nums1, nums2, nums3, nums4))  
            