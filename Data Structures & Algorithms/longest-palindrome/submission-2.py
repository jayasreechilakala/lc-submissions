class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        print(c)
        res = 0
        flag = False
        for k, v in c.items():
            if v % 2 == 0:
                res += v
            else:
                res += (v - v % 2) 
            if not flag and v % 2 == 1:
                flag = True
        return res + 1 if flag else res