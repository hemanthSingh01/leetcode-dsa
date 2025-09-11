class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp=[float("inf")]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                diff=i-coin
                if diff<0:
                    break
                else:
                    dp[i]=min(dp[i],1+dp[diff])
        return dp[amount] if dp[amount]!=float("inf") else -1