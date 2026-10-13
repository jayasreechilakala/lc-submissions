class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] < target:
                    l = mid + 1
                elif arr[mid] > target:
                    r = mid - 1
                elif arr[mid] == target:
                    return True
            return False
        for i in matrix:
            if i[0] <= target <= i[-1]:
                return binary_search(i)
            else:
                continue 
        return False