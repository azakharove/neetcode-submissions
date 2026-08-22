class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            mult = nums[:i] + nums[i+1:]
            prod = 1
            for number in mult:
                prod *= number
            output.append(prod)
        return output