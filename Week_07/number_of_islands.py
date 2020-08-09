class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.num_islands_dfs(grid)

    def num_islands_uf(self, grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        n = rows * cols
        uf = UnionFind(n + 1)

        def get_index(x, y):
            return x * cols + y

        directions = ((0, 1), (1, 0))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), n)
                if grid[i][j] == '1':
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if nx < rows and ny < cols and grid[nx][ny] == '1':
                            uf.union(get_index(i, j), get_index(nx, ny))

        return uf.get_count() - 1

    def num_islands_dfs(self, grid):
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        marked = [[False] * cols for _ in grid]
        count = 0
        xs = (0, 0, 1, -1)
        ys = (1, -1, 0, 0)
        directions = list(zip(xs, ys))

        def dfs(x: int, y: int):
            nonlocal directions, marked, rows, cols
            marked[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not marked[nx][ny] and grid[nx][ny] == '1':
                    dfs(nx, ny)

        for i in range(rows):
            for j in range(cols):
                if not marked[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count