class SolutionI:
    def __init__(self):
        self.values = []
    def inorderTraversal(self, A):
        if(A==None):
            return self.values
        self.inorderTraversal(A.left)
        self.values.append(A.val)
        self.inorderTraversal(A.right)
        return self.values

class SolutionPo:
    def __init__(self):
        self.values = []
    def postorderTraversal(self, A):
        if(A==None):
            return self.values
        self.postorderTraversal(A.left)
        self.postorderTraversal(A.right)
        self.values.append(A.val)
        return self.values

class SolutionPr:
    def __init__(self):
        self.values = []
    def preorderTraversal(self, A):
        if(A==None):
            return self.values
        self.values.append(A.val)
        self.preorderTraversal(A.left)
        self.preorderTraversal(A.right)
        
        return self.values