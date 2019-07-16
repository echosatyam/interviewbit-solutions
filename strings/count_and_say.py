class Solution:
    def countAndSay(self, A):
        if(A == 0 ):
            return ""
        s = "1"
        for i in range(A-1):
            prev = s[0:1]
            count = 1
            new_str = ''
            for j in range(1, len(s)):
                if(prev == s[j]):
                    count += 1
                else:
                    new_str += (str(count)+prev)
                    count = 1
                prev = s[j]
            new_str += (str(count)+prev)
            s = new_str
        return s

for i in range(15):
    print(Solution().countAndSay(i))
