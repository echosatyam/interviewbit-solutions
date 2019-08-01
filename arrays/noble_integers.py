class Solution:
    def solve(self, A):
        if len(A) < 1:
            return -1
        A.sort()
        i = 0
        while(i < len(A)-1):
            if A[i] != A[i+1] and A[i] == (len(A)-i-1):
                return 1
            i+=1
        if A[i]==0:
            return 1
        return -1



print(Solution().solve([ -4, -2, 0, -1, -6 ]))
