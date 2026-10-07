import itertools
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        tmp = 0
        c = defaultdict(list)
        for i in nums:
            c[i].append(i)
        for k, v in c.items():
            tmp = list(itertools.combinations(v, 2))
            res += len(tmp)
        return res
        