class Solution(object):
    def twoSum(self, nums, target):
        differences = {}
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in differences:
                return [i, differences[difference]]
            differences[nums[i]] = i
        return []