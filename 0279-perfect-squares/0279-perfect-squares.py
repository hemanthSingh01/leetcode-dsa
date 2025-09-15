class Solution:
    def numSquares(self, n: int) -> int:
        num=int(math.sqrt(n))
        nums=[i*i for i in range(1,num+1)]
        dp=[float("inf")]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for num in nums:
                diff=i-num
                if diff<0:
                    break
                else:
                    dp[i]=min(dp[i],1+dp[diff])
        return dp[n]
