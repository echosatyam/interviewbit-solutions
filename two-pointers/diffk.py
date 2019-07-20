""" 
Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

 Example: Input : 
    A : [1 3 5] 
    k : 4
 Output : YES as 5 - 1 = 4 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
 """

class Solution:
    def bin_search(self,A,low,high,x):
        if(low<=high):
            mid = int((high+low)/2)
            if A[mid]==x:
                return True
            elif A[mid]<x:
                return self.bin_search(A,mid+1,high,x)
            else:
                return self.bin_search(A,low,mid-1,x)
        return False
            
    def diffPossible(self, A, B):
        if(len(A)<=1):
            return 0
        Max = A[-1]
        for i in range(len(A)-1):
            if A[i]+B>Max:
                return 0
            if self.bin_search(A,i+1,len(A)-1,(A[i]+B)):
                return 1
        return 0
print(Solution().diffPossible([1,2,3,4,5,16],11))   