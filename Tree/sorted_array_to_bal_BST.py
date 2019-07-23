class Solution:
    def __init__(self):
        self.head = None

    def arrayToBST(self, A, low, high):
        if low <= high:
            mid = (high+low)//2
            node = TreeNode(A[mid])
            if(self.head == None):
                self.head = node
            node.left = self.arrayToBST(A, low, mid-1)
            node.right = self.arrayToBST(A, mid+1, high)
            return node
        return None

    def sortedArrayToBST(self, A):
        self.arrayToBST(A, 0, len(A)-1)
        return self.head
