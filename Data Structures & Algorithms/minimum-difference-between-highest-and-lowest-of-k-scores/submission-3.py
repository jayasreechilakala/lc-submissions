class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        r = 0
        ans = float('inf')
        tmp = 0
        for l in range(n - k + 1):
            r = l + k - 1
            tmp = nums[r] - nums[l]
            ans = min(tmp, ans)
        return ans
#  1 4 7 9
#  3