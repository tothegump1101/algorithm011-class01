"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def permute(choices: List[int], path: List[int]):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i, n in enumerate(choices):
                if i > 0 and choices[i-1] == n:
                    continue
                path.append(n)
                permute(choices[:i] + choices[i+1:], path)
                path.pop()

        permute(nums, [])
        return res
