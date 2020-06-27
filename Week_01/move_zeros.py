from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cur = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur], nums[i] = nums[i], nums[cur]
                cur += 1

    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_num = 0
        for n in nums:
            if n == 0:
                zero_num += 1
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[cur] = nums[i]
                cur += 1
        while cur < len(nums):
            nums[cur] = 0
            cur += 1
