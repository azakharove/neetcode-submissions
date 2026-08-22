class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        length = len(nums)
        while i < length:
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                return [min(i, nums.index(diff)), max(i, nums.index(diff))]
            else:
                i += 1