""" 
Prime Sum
Asked in:  
Epic systems
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d] 

If a < c OR a==c AND b < d. 
 """

class Solution1:
    def primesum(self, A):
        isprime = [True for i in range(A-1)]
        for i in range(2,A):
            if isprime[i-2]:
                for j in range(2*i,A,i):
                    isprime[j-2]=False
        for i in range(2,A//2+1):
            if isprime[i-2] and isprime[A-i-2]:
                return [i,A-i]
        
import math
class Solution2:
    def is_prime(self,A):
        root = int(math.sqrt(A))+1
        for i in range(2,root):
            if A%i==0:
                return False
        return True
    def primesum(self, A):
        for i in range(2,A//2+1):
            if(self.is_prime(i) and self.is_prime(A-i)):
                return [i,A-i]
print(Solution1().primesum(8))
print(Solution2().primesum(8))