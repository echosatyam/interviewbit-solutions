class Solution:
    def removeDuplicates(self, A):
        if(len(A) < 2):
            return len(A)
        prev = A[0]
        count = 1
        for i in range(1, len(A)):
            if(A[i] != prev):
                A[count] = A[i]
                count += 1
            prev = A[i]
        return A[:count] #return according to the question
print(Solution().removeDuplicates([ 1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9 ]))