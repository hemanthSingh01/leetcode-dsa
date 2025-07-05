class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
         l=0
         r=len(nums)-1
         f_i=-1
         l_i=-1
         while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                f_i=mid
                r=mid-1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
         l=0
         r=len(nums)-1
         while l<=r:
             mid=l+(r-l)//2
             if nums[mid]==target:
                l_i=mid
                l=mid+1
             elif nums[mid]>target:
                r=mid-1
             else:
                l=mid+1
         return [f_i,l_i]