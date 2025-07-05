from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr=nums.copy()
        nums.clear()
        dici=Counter(arr)
        for k,v in dici.items():
            if v>2:
                nums.extend([k]*2)
            else:
                nums.extend([k]*v)
        return len(nums)