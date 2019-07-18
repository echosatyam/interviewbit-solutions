""" 
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True  
as 2^2 = 4. 
 """


import math


class Solution:
    def isPower(self, A):
        # 2 is added in case of smaller numbers like 8
        root = int(math.sqrt(A))+2
        for i in range(2, root):
            val = math.pow(A, (1/i))
            # sometimes the values are not exactly same.
            diff = abs(val-round(val))
            if(diff < .000001):  # this is done for some calculation errors
                return 1
        return 0


print(Solution().isPower(8))
