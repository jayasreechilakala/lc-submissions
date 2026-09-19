class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        before, after = [0] * len(nums), [0] * len(nums)
        tmp = 0
        for i in range(1, len(nums)):
            tmp += nums[i - 1]
            before[i] = tmp
        tmp = 0
        for i in range(len(nums) - 2, -1, -1):
            tmp += nums[i + 1]
            after[i] = tmp

        for i in range(len(nums)):
            if before[i] == after[i]:
                return i

        return -1