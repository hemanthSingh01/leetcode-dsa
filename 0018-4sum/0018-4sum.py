class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l=[]
        nums.sort()
        n=len(nums)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                lo,hi=j+1,n-1
                while lo<hi:
                    summ=nums[i]+nums[j]+nums[lo]+nums[hi]
                    if summ==target:
                        l.append([nums[i],nums[j],nums[lo],nums[hi]])
                        lo,hi=lo+1,hi-1
                        while lo<hi and nums[lo]==nums[lo-1]:
                            lo=lo+1
                        while lo<hi and nums[hi]==nums[hi+1]:
                            hi=hi-1
                    elif summ<target:
                        lo=lo+1
                    else:
                        hi=hi-1
        return l
