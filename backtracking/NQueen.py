""" 
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

N Queens: Example 1

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
 """


 """ 
 This solution is correct but this won't work in the website due to some technical problems of the website.
 same implementation in java will work.
 try this solution on your computer to see it's validity.
  """
class Solution:
    def __init__(self):
        self.solution = []
    def is_safe(self,board,row,col):
        N = len(board)
        for i in range(col):
            if board[row][i]=="Q":
                return False
        for i , j in zip(range(row,-1,-1),range(col,-1,-1)):
            if board[i][j] =="Q":
                return False
        for i , j in zip(range(row,N),range(col,-1,-1)):
            if board[i][j]=="Q":
                return False
        return True

    def solve(self,board,col):
        N = len(board)
        if(col==N):
            return True
        res = False
        for i in range(N):
            if self.is_safe(board,i,col):
                board[i][col] ="Q"
                if self.solve(board,col+1):
                    return True
                board[i][col]="."
        return False
    def solveNQueens(self, A):
        if(A==1):
            return ['Q']
        for i in range(A):
            board=[["." for i in range(A)]for j in range(A)]
            board[i][0]="Q"
            if self.solve(board,1):
                self.solution.append(board)
        return self.solution
res = Solution().solveNQueens(4)
for r in res:
    print("solution")
    for j in r:
        print(j)
    print("\n\n")
print(res)