""" 
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.
"""
class Solution:
    def solve(self, A, B, C):
        Min_diff = abs(max(A[0],B[0],C[0])-min(A[0],B[0],C[0]))
        first_pointer = 0
        middle_pointer=0
        last_pointer = 0
        while(first_pointer<len(A)  and middle_pointer<len(B) and last_pointer<len(C)):
            min_element = min(A[first_pointer],B[middle_pointer],C[last_pointer])
            max_element = max(A[first_pointer],B[middle_pointer],C[last_pointer])
            if abs(min_element-max_element)<Min_diff:
                Min_diff= abs(min_element-max_element)
            if min_element ==A[first_pointer]:
                first_pointer+=1
            if min_element == B[middle_pointer]:
                middle_pointer+=1
            if min_element == C[last_pointer]:
                last_pointer+=1
        return Min_diff