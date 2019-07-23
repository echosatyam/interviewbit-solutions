""" 

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Example :

Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

"""


class Solution:
    def findSum(self,A,B,weight):
        if A.right==None and A.left ==None and weight+A.val == B:
            return 1
        if A.right==None and A.left ==None and weight+A.val != B:
            return 0
        left = 0
        right = 0
        if(A.left!=None):
            left = self.findSum(A.left,B,weight+A.val)
        if(A.right!=None):
            right = self.findSum(A.right,B,weight+A.val)
        return left or right
        
    def hasPathSum(self, A, B):
        return self.findSum(A,B,0)
        