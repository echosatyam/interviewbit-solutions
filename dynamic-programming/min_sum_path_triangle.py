import sys
class Solution:
    def minimumTotal(self, A):
        if len(A)==0 or len(A[0])==0:
            return 0
        dp = [[0 for i in range(len(A[j]))] for j in range(len(A))]
        dp[0][0]=A[0][0]
        for i in range(1,len(A)):
            for j in range(len(A[i])):
                min1 = A[i-1][j] if j<len(A[i-1]) and j>=0 else sys.maxsize
                min2 = A[i-1][j-1]  if j-1<len(A[i-1]) and j-1>=0 else sys.maxsize
                A[i][j] = min(min1,min2)+A[i][j]
        return min(A[len(A)-1])