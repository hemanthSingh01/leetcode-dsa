from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr=nums.copy()
        nums.clear()
        dici=Counter(arr)
        for i in dici.keys():
            nums.append(i)
        return(len(nums))
        