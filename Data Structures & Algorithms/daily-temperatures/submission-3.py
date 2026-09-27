class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stk = []
        n = len(temperatures)
        res = [0] * n
        i = n - 2
        stk.append(n - 1)
        while i >= 0:
            while stk and temperatures[i] >= temperatures[stk[-1]] and i >= 0:
                stk.pop()
            else:
                res[i] = stk[-1] - i if stk else 0
                stk.append(i)
                i -= 1
        return res