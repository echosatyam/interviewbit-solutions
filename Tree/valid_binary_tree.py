""" 
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
Both the left and right subtrees must also be binary search trees.
Example :

Input : 
   1
  /  \
 2    3

Output : 0 or False


Input : 
  2
 / \
1   3

Output : 1 or True 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem


 """
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBSTq(self, node,mini,maxi):
        if node==None:
            return True
        if  node.val <mini or node.val> maxi:
            return False
        left = self.isValidBSTq(node.left,mini,node.val-1)
        right = self.isValidBSTq(node.right,node.val+1,maxi)   
        return left and right 
    def isValidBST(self, A):
        if(self.isValidBSTq(A,-1e9,1e9)):
            return 1
        return 0