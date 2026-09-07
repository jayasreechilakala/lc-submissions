class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        print(c)
        a = 0
        for b, v in c.items():
            if v == 1:
                a += 1
            if (v == 1 and a == k):
                return b
        return ""