class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        n=len(nums)
        arr=[[] for i in range(n)]
        for i in nums:
            arr[0].append(i)
        idx=0
        j=1
        while len(arr[idx])>1:
            for i in range(len(arr[idx])-1):
                add=(arr[idx][i]+arr[idx][i+1])%10
                arr[j].append(add)
            idx+=1
            j+=1
        return arr[-1][0]