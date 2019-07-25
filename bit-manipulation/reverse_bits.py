
""" 
Reverse Bits
Asked in:  
Nvidia
HCL
Amazon
Reverse bits of an 32 bit unsigned integer

Example 1:

x = 0,

          00000000000000000000000000000000  
=>        00000000000000000000000000000000
return 0

Example 2:

x = 3,

          00000000000000000000000000000011 
=>        11000000000000000000000000000000
return 3221225472

Since java does not have unsigned int, use long
 """


class Solution:
    def reverse(self, A):
        return int(bin(A)[2:].zfill(32)[::-1],2)
        
print(Solution().reverse(131241))