class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        ans1 = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                ans += 1
                res = max(res, ans)
            else:
                ans = 1
            if nums[i - 1] > nums[i]:
                ans1 += 1
                res = max(res, ans1)
            else:
                ans1 = 1
        return res
        