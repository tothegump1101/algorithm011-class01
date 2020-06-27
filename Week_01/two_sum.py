class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        cache = dict()
        for index, num in enumerate(nums):
            if (target - num) in cache:
                return [cache[target - num], index]
            cache[num] = index
        return []
