

class Solution:
    def intersection(self,A,B):
        a_pointer = 0
        b_pointer = 0
        res =[]
        while(a_pointer<len(A) and b_pointer<len(B)):
            if((A[a_pointer]==B[b_pointer])):
                res.append(A[a_pointer])
                a_pointer+=1
                b_pointer+=1
            elif(A[a_pointer]<B[b_pointer]):
                a_pointer+=1
            else:
                b_pointer+=1
        return res
    def intersect(self, A, B):
        return self.intersection(list(A),list(B))
print(Solution().intersection([1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9]))