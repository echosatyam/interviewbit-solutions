class Solution:
    def minPathSum(self, A): 
        if len(A)==0 or len(A[0])==0:
            return 0
        n = len(A)
        m = len(A[0])
        dp = [[0 for i in range(m)] for j in range(n)]
        dp[0][0]=A[0][0]
        for i in range(1,n):
            dp[i][0] = dp[i-1][0]+A[i][0]
        for j in range(1,m):
            dp[0][j] = dp[0][j-1]+A[0][j]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+A[i][j]
        return dp[n-1][m-1]
