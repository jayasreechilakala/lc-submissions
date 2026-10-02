class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        a = Counter(chars)
        res = 0
        for i in words:
            b = Counter(i)
            tmp = 0
            for j in i:
                if (j not in a or b[j] > a[j]): 
                    continue
                else:
                    tmp += 1
            if tmp == len(i):
                res += len(i)
        return res