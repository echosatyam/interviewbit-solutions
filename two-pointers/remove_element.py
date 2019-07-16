'''
Remove element from the array
'''
class Solution:
   
    def removeElement(self, A, B):
        count = 0
        for i in range(len(A)):
            if(A[i]!=B):
                A[count] = A[i]
                count+=1
        return A[:count]
print(Solution().removeElement([ 1, 1, 2, 3, 3, 4, 4, 5, 1, 6, 6, 1, 1, 9 ],1))
