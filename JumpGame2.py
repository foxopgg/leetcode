class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        farthest = 0
        currentEnd = 0
        jumps = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == currentEnd:
                jumps += 1
                currentEnd = farthest
                if currentEnd >= n - 1:
                    break
        return jumps