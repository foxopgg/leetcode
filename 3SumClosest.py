class Solution(object):
    def threeSumClosest(self, nums, target):
        closestSum = float('inf')
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = length - 1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if abs(target - sum3) < abs(target - closestSum):
                    closestSum = sum3
                if sum3 > target:
                    k -= 1
                elif sum3 < target:
                    j += 1
                else:
                    return sum3
        return closestSum