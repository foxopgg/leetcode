class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(i, current, total):
            if total == target:
                result.append(current[:])
                return
            if i >= len(candidates) or total > target:
                return
            
            current.append(candidates[i])
            backtrack(i, current, candidates[i] + total)
            current.pop()

            backtrack(i + 1, current, total)
        
        backtrack(0, [], 0)
        return result