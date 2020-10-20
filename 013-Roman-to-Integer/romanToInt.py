# 分かりやすい
class Solution:
    def romanToInt(self, s: str) -> int:
        # rn = roman_numerals
        rn = {"I":1, "V":5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000}
        r = 0
        for i in range(0, len(s) - 1):
            if rn[s[i]] < rn[s[i+1]]:
                r -= rn[s[i]]
            else:
                r += rn[s[i]]
        return r + rn[s[-1]]

# こっちのほうが早い
    
class Solution:
    def romanToInt(self, s):
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        z, p = 0, 'I'
        for c in s[::-1]:
            z, p = z - d[c] if d[c] < d[p] else z + d[c], c
            print(z, p)
        return z