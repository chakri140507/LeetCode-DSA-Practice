class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        r = len(matrix)
        col = len(matrix[0])
        ans = []
        for i in range(col):
            ans.append([0]*r)

        for i in range(col):
            for j in range(r):
                ans[i][j] = matrix[j][i]
        return ans

