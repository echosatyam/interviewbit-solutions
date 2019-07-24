class Solution:
    def maxProfit(self, A):
        if(len(A)<2):
            return 0
        Min = min(A)
        Max = max(A)
        dp =[[0,0]for i in range(len(A))]
        dp[0][0] = A[0]
        dp[len(A)-1][1]=A[len(A)-1]
        for num in range(1,len(A)):
            if(dp[num-1][0]>A[num]):
                dp[num][0]=A[num]
            else:
                dp[num][0]=dp[num-1][0]
        for num in range(len(A)-2,-1,-1):
            if(dp[num+1][1]<A[num]):
                dp[num][1]=A[num]
            else:
                dp[num][1] =dp[num+1][1]
        max_profit = 0
        for element in dp:
            profit = element[1]-element[0]
            if(profit>max_profit):
                max_profit = profit
        return max_profit
