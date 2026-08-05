class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        n = len(temperatures)
        ans = [0] * n
        stk.append(n - 1)
        n -= 2
        while n >= 0 and stk:
            while stk and temperatures[n] >= temperatures[stk[-1]]:
                stk.pop()
            if stk:
                ans[n] = stk[-1] - n
            else:
                ans[n] = 0

            stk.append(n)
            n -= 1
                        
            
        return ans
