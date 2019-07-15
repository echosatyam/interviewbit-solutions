'''
Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
 NOTE : k is 0 based. k = 0, corresponds to the row [1]. 

'''


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def getRow(self, A):
        pascal = [[1 for i in range(j+1)] for j in range(A+1)]

        if(A > 2):
            for i in range(2, A+1):
                for j in range(1, i):
                    pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]
            print(pascal)
        return pascal[A]
