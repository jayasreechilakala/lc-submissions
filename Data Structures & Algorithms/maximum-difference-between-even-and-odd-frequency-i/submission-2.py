class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        a1, a2 = float('inf'), float('-inf')
        a3, a4 = float('-inf'), float('inf')
        for k, v in c.items():
            if v % 2 != 0:
                a1 = min(a1, v)
            else:
                a2 = max(a2, v)
        for k, v in c.items():
            if v % 2 != 0:
                a1 = max(a1, v)
            else:
                a2 = min(a2, v)
        return max(a1 - a2, a3 - a4)