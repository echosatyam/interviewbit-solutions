""" 
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
 """

import operator

allowed_operators={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
class Solution:
    def evalRPN(self, A):
        if(len(A)==0):
            return ""
        if(len(A)==1):
            return A[0]
        stack = []
        operands =["+", "-", "*", "/"]
        for element in A:
            if element not in operands:
                stack.append(element)
            else :
                two = int(stack.pop())
                one = int(stack.pop())
                stack.append(int(allowed_operators[element](one,two)))
        return stack[-1]
print(Solution().evalRPN(["2", "1", "+", "3", "*"]))