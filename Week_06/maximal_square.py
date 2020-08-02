"""
221. 最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        max_num = 0

        for row in range(rows):
            dp[row][0] = int(matrix[row][0])
            max_num = max(max_num, dp[row][0])
        for col in range(1, cols):
            dp[0][col] = int(matrix[0][col])
            max_num = max(max_num, dp[0][col])

        def go_on(r, c, l):
            if r - l < 0:
                return False
            if c - l < 0:
                return False
            return matrix[r][c - l] == '1' and matrix[r - l][c] == '1'
        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == '0':
                    dp[row][col] = 0
                else:
                    length = 0
                    while length < dp[row - 1][col - 1] and go_on(row, col, length + 1):
                        length += 1
                    dp[row][col] = length + 1
                max_num = max(max_num, dp[row][col])
        return max_num ** 2
