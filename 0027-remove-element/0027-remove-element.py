class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr=nums.copy()
        nums.clear()
        for i in arr:
            if i!=val:
                nums.append(i)
        return len(nums)