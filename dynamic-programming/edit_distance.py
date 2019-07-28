import numpy
class Solution:
    def minDistance(self, A, B):
        m , n = len(A), len(B)
        if m==0 or n==0:
            return m if m!=0 else n
        dp= [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                elif A[i-1]==B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j]=1+ min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                # print(numpy.asarray(dp))
        
        return dp[m][n]

print(Solution().minDistance("abcd","asdaddf"))