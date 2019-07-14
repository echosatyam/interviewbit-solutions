'''
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:

		
Input: 	

1 2 3
4 5 6
7 8 9

Return the following :

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input : 
1 2
3 4

Return the following  : 

[
  [1],
  [2, 3],
  [4]
]

'''


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        R=[]
        for i in range(2*n-1):
            B=[]
            counter = i 
            if i<n:
                start = 0
                end = counter
                while(start<n and end>-1):
                    B.append(A[start][end])
                    start+=1
                    end-=1
            else:
                start = counter-n+1
                end  = n-1
                while(start<n and end>-1):
                    B.append(A[start][end])
                    start+=1
                    end-=1
            R.append(B)
        return R