class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            width = right - left
            if height[left] > height[right]:
                maxArea = max(maxArea, height[right] * width)
                right -= 1
            else:
                maxArea = max(maxArea, height[left] * width)
                left += 1
        return maxArea