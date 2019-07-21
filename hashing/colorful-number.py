class Solution:
    def colorful(self, A):
        A = str(A)
        if(len(A)==1):
            return 1
        s = [int(a) for a in A]
        if(len(s)>len(set(s))):
            return 0
        for i in range(1,len(A)):
            for j in range(len(A)-i):
                prod =1
                for k in range(j,j+i+1):
                    prod*=(int(A[k]))
                s.append(prod)
            if(len(s)>len(set(s))):
                return 0
        return 1
print(Solution().colorful(1232143))