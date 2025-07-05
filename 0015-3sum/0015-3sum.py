class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums.sort()
        n=len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            lo,hi=i+1,n-1
            while lo<hi:
                summ=nums[i]+nums[lo]+nums[hi]
                if summ==0:
                    l.append([nums[i],nums[lo],nums[hi]])
                    lo,hi=lo+1,hi-1
                    while lo<hi and nums[lo]==nums[lo-1]:
                        lo=lo+1
                    while lo<hi and nums[hi]==nums[hi+1]:
                        hi=hi-1
                elif summ<0:
                    lo=lo+1
                else:
                    hi=hi-1
        return l
