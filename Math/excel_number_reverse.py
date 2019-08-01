class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        s=""
        i=1
        while A>0:
            remainder = A%26
            s+=chr((remainder)+64) if remainder!=0 else "Z"
            A= A//26 if remainder!=0 else (A//26 -1)
        return s[::-1]
print(Solution().convertToTitle(943566))