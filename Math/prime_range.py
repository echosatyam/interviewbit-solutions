class Solution:
    def sieve(self, A):
        if A<2:
            return []
        isprime = [True for i in range(A+1)]
        isprime[0]=False
        isprime[1]=False
        res = []
        for i in range(2,A+1):
            if isprime[i]:
                res.append(i)
                for j in range(i*2,A+1,i):
                    isprime[j]=False
        
        return res
print(Solution().sieve(10))