class Solution(object):
    def permuteUnique(self, nums):
        result, visited = [], [False] * len(nums)
        nums.sort()
        self.dfs(nums, visited, [], result)
        return result

    def dfs(self, nums, visited, path, result):
        if len(nums) == len(path):
            result.append(path)
            return
        for i in range(len(nums)):
            if not visited[i]:
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:
                    continue
                visited[i] = True
                self.dfs(nums, visited, path+[nums[i]], result)
                visited[i] = False