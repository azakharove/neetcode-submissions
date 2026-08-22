class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_nums = list(set(nums))
        unique_nums.sort()

        longest = 1
        current = 1

        for i in range(1, len(unique_nums)):
            if unique_nums[i] == unique_nums[i - 1] + 1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)

        return longest
