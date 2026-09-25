class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        ls, lg = 0, 0
        while (ls < len(s) and lg < len(g)):
            if s[ls] >= g[lg]:
                res += 1
                ls += 1
                lg += 1
            else:
                ls += 1
        return res 