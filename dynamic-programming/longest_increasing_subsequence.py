class Solution:
    def lis(self, A):
        n = len(A)
        if n<=1:
            return n
        dp= [1 for i in range(n)]
        for i in range(1,n):
            for j in range(i):
                if A[i]>A[j] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
        return max(dp)
    