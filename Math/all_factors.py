'''
Find all factors of a given number
'''

import math


class Solution:
    def allFactors(self, A):
        if A < 2:
            return [A]
        limit = int(math.sqrt(A))
        left = []
        right = []
        for i in range(1, limit+1):
            if(A % i == 0):
                left.append(i)
                if(i != A//i):
                    right.insert(0, A//i)
        left.extend(right)
        return left


print(Solution().allFactors(82900))
