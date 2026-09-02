class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=3:
            return n
        a = 1
        b = 1
        c = 0
        for i in range(n - 1):
            print(a, b, c)
            c = a + b
            a = b
            b = c
            
        return c