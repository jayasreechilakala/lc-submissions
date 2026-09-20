class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        res = 0
        left, right = float('-inf'), float('-inf')
        while i < j:
            left = max(left, height[i])
            right = max(right, height[j])
            if height[i] < height[j]:
                res += min(left, right) - height[i]
                i += 1
            else:
                res += min(left, right) - height[j]
                j -= 1
        return res

