class Solution:
    def flip(self, A):
        if(A.count('1')==len(A)):
            return []
        n = len(A)
        max_here = 0
        start_here=0
        end_here=0
        max_sum = -1*n
        start_min = len(A)
        end_min = len(A)
        for i in range(n):
            if(max_here<0):
                max_here = 0
                start_here=i
                end_here=i
            max_here = max_here+ (1 if A[i]=='0' else -1)
            if (max_here>max_sum):
                max_sum = max_here
                start_min=start_here
                end_min=end_here
            
            end_here+=1
        return [start_min+1,end_min+1]

sol = Solution()
print(sol.flip('01010100'))
