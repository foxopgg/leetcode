class Solution(object):
    def longestCommonPrefix(self, strs):
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        result = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            result += first[i]
        return result