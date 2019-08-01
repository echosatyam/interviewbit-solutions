class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        number = 0
        for place in range(len(A)):
            # print(ord(A[place])-64)
            number+=26**(len(A)-place-1)*(ord(A[place])-64)
        return number
print(Solution().titleToNumber("AAA"))