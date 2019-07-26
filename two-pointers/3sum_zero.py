
""" 
3 Sum Zero
Asked in:  
Facebook
Google
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2) 
 """


class Solution:
    def threeSum(self, A):
        if(len(A)<3):
            return []
        A.sort()
        ans = []
        n=len(A)
        for i in range(0,n-1):
            first = i
            middle = i+1
            last = n-1
            while(middle<last):
                if(A[first]+A[middle]+A[last]==0 and first!=middle and last!=first ):
                    ans.append([A[first],A[middle],A[last]])
                    last-=1
                    middle+=1
                elif(A[first]+A[middle]+A[last]>=0):
                    last-=1
                else:
                    middle+=1
        s=[]
        for i in ans:
            if i not in s:
                s.append(i)
        return s
print(Solution().threeSumClosest([ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]))