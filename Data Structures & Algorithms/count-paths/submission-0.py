class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        U = [[1] * n for _ in range(m)]

        for r in range(1,m):
            for c in range(1,n):
                U[r][c] = U[r-1][c] + U[r][c-1]

        return U[m-1][n-1]