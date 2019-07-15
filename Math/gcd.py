class Solution:
    def gcd(self, a, b):
        while(b > 0):
            a, b = b, a % b
        return a


sol = Solution()
print(sol.gcd(0, 10))
