class Solution(object):
    def threeSum(self, nums):
        length = len(nums)
        result = []
        nums.sort()
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = length - 1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 > 0:
                    k -= 1
                elif sum3 < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return result