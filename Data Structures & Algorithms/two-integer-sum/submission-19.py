class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        j = 0
        length = len(nums)
        while i < length:
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                    if i < nums.index(diff):
                        return [i, nums.index(diff)]
                    else:
                        return [nums.index(diff), i]
            else:
                i += 1