def numRange(A, B, C):
        dp= [[ 0 for i in range(len(A))] for j in range(len(A))]
        count=0
        for i in range(len(A)):
            for j in range(i,len(A)):
                if i==j:
                    dp[i][j]=A[i]
                else:
                    dp[i][j] = A[j]+dp[i][j-1]
                
                if B<=dp[i][j] <=C:
                    count+=1
        print(dp)
        return count
        
numRange([1,2,3,4,5,],5,6)