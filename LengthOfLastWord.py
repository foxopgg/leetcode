class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        lastCount = 0
        for i in s:
            if i == " ":
                if count > 0:
                    lastCount = count
                    count = 0
                else:
                    continue
            else:
                count += 1
        if count == 0:
            return lastCount
        return count