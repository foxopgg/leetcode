class Solution(object):
    def searchRange(self, nums, target):
        def findBoundary(nums, start, end, target, findFirst = False):
            ans = -1
            while start <= end:
                middle = (start + end) // 2
                if nums[middle] < target:
                    start = middle + 1
                elif nums[middle] > target:
                    end = middle - 1
                else:
                    ans = middle
                    if findFirst:
                        end = middle - 1 
                    else:
                        start = middle + 1
            return ans

        length = len(nums)
        left = findBoundary(nums, 0, length - 1, target, True)
        return [left, findBoundary(nums, 0, length - 1, target)]