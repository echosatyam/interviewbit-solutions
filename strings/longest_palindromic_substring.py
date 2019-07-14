





'''
This solution is being referred from geeks for geeks

'''
class Solution:
    
    def longestPalindrome(self, A):
        n= len(A)
        if(n<=1):
            return A
        if(n==2):
            if(A[0]==A[1]):
                return A
            else:
                return A[0]
        dp = [[False for i in range(n)]for j in range(n)]
        for i in range(n):
            dp[i][i]=True
        MAX = 0
        start=0
        i=0
        while i < n - 1 : 
            if (A[i] == A[i + 1]) : 
                dp[i][i + 1] = True
                start = i 
                MAX = 2
            i = i + 1
        for k in range(3,n+1):
            for i in range(n-k+1):
                j = i+k-1
                if(dp[i+1][j-1]and A[i]==A[j]):
                    dp[i][j]=True
                    if(k>MAX):
                        MAX = k
                        start = i
        
        return A[start:start+MAX]
print(Solution().longestPalindrome("abacdf"))