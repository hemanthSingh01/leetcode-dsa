class Solution(object):
    def twoSum(self, nums, target):
        dici={}
        for i,num in enumerate(nums):
            c=target-num
            if c in dici:
                return ([dici[c],i])
            dici[num]=i
        