class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = False
        occurences = set()
        for x in nums:
            if x in occurences:
                duplicate = True
                return duplicate

            else:
                occurences.add(x)
        return duplicate