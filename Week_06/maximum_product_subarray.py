"""
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp_max = [0] * len(nums)
        dp_min = [0] * len(nums)
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i])
                dp_min[i] = min(dp_min[i - 1] * nums[i], nums[i])
            else:
                dp_max[i] = max(dp_min[i - 1] * nums[i], nums[i])
                dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i])
        return max(dp_max)
