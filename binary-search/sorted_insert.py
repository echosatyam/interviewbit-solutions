class Solution:
    def searchInsert(self, A, element):
        low,high = 0,len(A)-1
        while(low<=high):
            mid = (high+low)//2
            ## simply adding two conditions by checking side elements 
            if A[mid]==element or( mid>0 and A[mid]>element and A[mid-1]<element):
                return mid 
            elif (mid <len(A)-1 and A[mid]<element and A[mid+1]>element):
                return mid+1
            elif  element>A[mid]:
                low = mid+1
            else:
                high=mid-1
        return low # returning low in case the boundary merged.