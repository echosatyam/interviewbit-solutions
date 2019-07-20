""" 
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack? 
A: In this case, return -1.

Q: What should pop do on empty stack? 
A: In this case, nothing. 

Q: What should top() do on empty stack?
A: In this case, return -1
 NOTE : If you are using your own declared global variables, make sure to clear them out in the constructor. 
 """

class MinStack:
    def __init__(self):
        self.stack = []
        self.Min = []
    def push(self, x):
        if(len(self.Min)==0 or x<self.getMin()):
            self.Min.append(x)
        self.stack.append(x)
    def pop(self):
        if len(self.stack):
            if(self.getMin()==self.top()):
                self.Min.pop()
            return self.stack.pop()
    def top(self):
        if len(self.stack):
            return self.stack[-1]
        return -1
    def getMin(self):
        if len(self.Min):
            return self.Min[-1]
        return -1
