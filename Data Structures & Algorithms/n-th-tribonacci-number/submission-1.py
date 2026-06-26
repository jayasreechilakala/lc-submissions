class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        for i in range(3, n + 1):
            tmp = a + b + c
            a = b
            b = c
            c = tmp
            print(a, b, c)
        return c

