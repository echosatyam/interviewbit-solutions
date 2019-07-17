'''
Generate al Paranthesis 
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

'''


class Solution:
    def isValid(self, A):
        stack = []
        brackets = {']': '[', '}': '{', ')': '('}
        for i in A:
            if(i in brackets.values()):
                stack.append(i)
            elif i in brackets.keys() and len(stack) > 0 and brackets[i] == stack[-1]:
                stack.pop()
            else:
                return 0
        if(len(stack) > 0):
            return 0
        return 1


print(Solution().isValid('{]'))
