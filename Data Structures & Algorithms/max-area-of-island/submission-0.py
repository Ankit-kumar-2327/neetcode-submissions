class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 1):
                    count = [0] * 1
                    self.dfs(i, j, dr, dc, grid, count)
                    ans = max(ans, count[0])
        
        return ans
        
    def dfs(self, r, c, dr, dc, grid, count):
        count[0] += 1
        grid[r][c] = 0

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if(nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1):
                self.dfs(nr, nc, dr, dc, grid, count)