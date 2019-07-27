""" 
You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

**abs(x) is absolute value of x and is implemented in the following manner : **

      if (x < 0) return -x;
      else return x;
Example :

Input : 
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]

Output : 5 
         With 10 from A, 15 from B and 10 from C.
 """


class Solution:
    def minimize(self, A, B, C):
        if len(A)==0 or len(B) ==0 or len(C)==0:
            return 2147483647
        i ,j, k= 0,0,0
        val = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
        while i<len(A) and j<len(B)and k <len(C):
            minimum = min(A[i],B[j],C[k])
            val=min(val,max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])))
            if minimum==A[i]:
                i+=1
            elif minimum ==B[j]:
                j+=1
            elif minimum==C[k]:
                k+=1
        return val      