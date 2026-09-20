class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0] * n, [0] * n
        res = 0
        left[0] = height[0]
        right[n - 1] = height[n - 1]
        tmp = float('-inf')
        for i in range(0, n):
            tmp = max(tmp, height[i])
            left[i] = tmp

        tmp = float('-inf')
        for i in range(n - 1, -1, -1):
            tmp = max(tmp, height[i])
            right[i] = tmp
        for i in range(n):
            res += min(left[i], right[i]) - height[i]
        return res