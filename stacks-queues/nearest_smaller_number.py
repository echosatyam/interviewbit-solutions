""" 
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Example:

Input : A : [4, 5, 2, 10, 8]
Return : [-1, 4, -1, 2, 2]

Example 2:

Input : A : [3, 2, 1]
Return : [-1, -1, -1]
 """

class Solution:
    def prevSmaller(self, A):
        if(len(A) == 1):
            return [-1]
        stack = [A[0]]
        l = [-1 for i in range(len(A))]
        for i in range(1, len(A)):
            while len(stack) != 0 and stack[-1] >= A[i]:
                stack.pop()
            if len(stack):
                l[i] = stack[-1]
            stack.append(A[i])
        return l
print(Solution().prevSmaller([4, 5, 2, 10, 8]))