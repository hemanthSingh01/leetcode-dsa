class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum=float("inf")
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                curr_sum=nums[i]+nums[l]+nums[r]
                if abs(curr_sum-target)<abs(closest_sum-target):
                    closest_sum=curr_sum
                if curr_sum==target:
                    return curr_sum
                elif curr_sum<target:
                    l+=1
                else:
                    r-=1
        return closest_sum