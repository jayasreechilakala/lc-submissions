class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a, b = False, False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                if b:
                    return False
                else:
                    a = True
            elif (a and nums[i] > nums[i + 1]):
                return False
            elif nums[i] > nums[i + 1]:
                b = True
            elif b and nums[i] < nums[i + 1]:
                if a:
                    return False
                else:
                    return False
        return True