class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        marea = 0
        while left < right:
            if heights[left] <= heights[right]:
                marea = max(marea, heights[left] * (right - left))
                left += 1
            if heights[right] < heights[left]:
                marea = max(marea, heights[right] * (right - left))
                right -=1
        return marea