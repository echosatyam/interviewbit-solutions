class Solution:
    def __init__(self):
        self.answers={}
    def pow(self, x, n, d):
        if x ==0:
            return 0
        if n==0:
            return 1
        if n in self.answers:
            return self.answers[n]
        if n%2==0:
            self.answers[n]= (self.pow(x,n//2,d)**2)%d
        else:
            self.answers[n]= ((self.pow(x,n//2,d)**2)*x)%d
        return self.answers[n]
print(Solution().pow(123412,1112,50000))