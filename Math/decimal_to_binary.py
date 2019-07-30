class Solution:
    def findDigitsInBinary(self, A):
        if A<=1:
            return A
        bin=""
        while(A>0):
            rem = A%2
            A = A//2
            bin = str(rem)+bin
        return bin
            
print(bin(100)[2:])            
print(Solution().findDigitsInBinary(100))