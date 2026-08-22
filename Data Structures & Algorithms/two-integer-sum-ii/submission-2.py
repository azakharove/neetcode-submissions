class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(numbers):
            indices[n] = i

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i+1, indices[diff]+1]
        return []