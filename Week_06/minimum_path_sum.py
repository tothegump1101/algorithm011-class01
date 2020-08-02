"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        dp = [0] * col
        dp[0] = grid[0][0]
        for i in range(1, col):
            dp[i] = grid[0][i] + dp[i - 1]
        for r in range(1, row):
            dp[0] += grid[r][0]
            for c in range(1, col):
                dp[c] = grid[r][c] + min(dp[c - 1], dp[c])
        return dp[-1]

    def minPathSum1(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        dp = [[0] * col for _ in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(1, col):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for r in range(1, row):
            for c in range(1, col):
                dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c - 1])
        return dp[-1][-1]
