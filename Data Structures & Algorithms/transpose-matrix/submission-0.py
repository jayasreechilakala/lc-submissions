class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        res = [[0] * r for i in range(c)]
        for i in range(r):
            for j in range(c):
                if i != j:
                    res[j][i] = matrix[i][j]
                else:
                    res[i][j] = matrix[i][j]

        return res