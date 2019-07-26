""" 
3 Sum
Asked in:  
Facebook
Amazon
Microsoft
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers.

Assume that there will only be one solution

Example: 
given array S = {-1 2 1 -4}, 
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
 """

class Solution:
    def threeSumClosest(self, A, B):
        if(len(A)<3):
            return 0
        A.sort()
        n=len(A)
        Min =abs(B-(A[0]+A[1]+A[2])) 
        Sum =A[0]+A[1]+A[2]
        for i in range(0,n-1):
            first = i
            middle = i+1
            last = n-1
            while(middle<last):
                S=A[first]+A[middle]+A[last]
                if(abs(B-S)<Min):
                    Min = abs(B-S)
                    Sum= S
                if(A[first]+A[middle]+A[last]==B):
                    return B
                elif(A[first]+A[middle]+A[last]>B):
                    last-=1
                else:
                    middle+=1
        return Sum
print(Solution().threeSumClosest([ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ],21))