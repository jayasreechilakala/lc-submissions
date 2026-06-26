class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        c2 = Counter(arr2)
        res = []
        tmp = []
        for i in arr2:
            if i in c:
                print(i)
                res += ([i] * c[i])
        for i in arr1:
            if i not in c2:
                tmp.append(i)
        tmp.sort()
        return res + tmp
