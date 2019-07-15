'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
**Example 2 : **
ABCD, 2 can be written as

A....C
...B....D
and hence the answer would be ACBD.
'''


class Solution:
    def convert(self, A, B):
        if(B == 1):
            return A
        n = len(A)
        elements = 2*(B-1)
        times = n//elements+1
        i = 0
        lists = [[] for x in range(B)]
        position = 0
        while(i < times):
            j = 0
            while(j < elements):
                index = j if(j <= B-1) else elements-j
                if(position < n):
                    lists[index].append(A[position])
                else:
                    lists[index].append('')
                position += 1
                j += 1
            i += 1

        s = ''
        for j in lists:
            s += "".join(j)
        return s


print(Solution().convert('THISISASTRING', 4))
