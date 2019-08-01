class Solution:
    def uniquePathsWithObstacles(self, A):
        m = len(A)
        n = len(A[0])
        if m==0 or n==0:
            return 0
        dp = [[0 for i in range(n) ]for j in range(m)]
        if A[0][0]==0:
            dp[0][0]=1
        for i in range(1,m):
            if A[i][0]==0:
                dp[i][0]=dp[i-1][0]
        for i in range(1,n):
            if A[0][i]==0:
                dp[0][i]=dp[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                if A[i][j]==0 :
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
A =[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(Solution().uniquePathsWithObstacles(A))