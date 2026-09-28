class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stk = []
        n = len(temperatures)
        res = [0] * n
        i = 1
        stk.append(0)
        while i < n:
            while stk and temperatures[stk[-1]] < temperatures[i] and i < n:
                j = stk.pop()
                res[j] = i - j
            stk.append(i)
            i += 1
        return res


