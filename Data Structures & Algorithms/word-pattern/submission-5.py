class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        c = {}
        d = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        i, j = 0, 0
        while i < len(pattern):
            if s[j] not in c:
                c[s[j]] = pattern[i]
            elif (s[j] in c and c[s[j]] != pattern[i]):
                return False
            if pattern[i] not in d:
                d[pattern[i]] = s[j]
                i += 1
                j += 1
            elif (pattern[i] in d and d[pattern[i]] != s[j]):
                return False
            else:
                i += 1
                j += 1
        print(c)
        return True