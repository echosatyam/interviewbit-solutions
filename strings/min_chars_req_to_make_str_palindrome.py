'''
You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string

Example:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2
'''


class Solution:
    def computeLPSArray(self, pat):

        pat = pat+"+"+pat[::-1]
        M = len(pat)
        l = 0
        lps = [0 for i in range(M)]
        i = 1
        while i < M:
            if pat[i] == pat[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps[-1]

    def solve(self, A):
        if(len(A) <= 2):
            return 0
        n = len(A)
        x = self.computeLPSArray(A)
        return n-x


print(Solution().solve("AABA"))
