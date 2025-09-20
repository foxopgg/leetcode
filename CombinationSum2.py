class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        combination = []
        self.backtrack(candidates, target, 0, combination, result)
        return result
    
    def backtrack(self, candidates, target, start, combination, result):
        if target == 0:
            result.append(list(combination))
            return
        for i in range(start, len(candidates)):
            #Check for duplicates
            if i > start and candidates[i] == candidates [i - 1]:
                continue
            if candidates[i] > target:
                break
            combination.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i + 1, combination, result)
            combination.pop()