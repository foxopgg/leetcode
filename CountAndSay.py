class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        else:
            return self.rle(self.countAndSay(n - 1))
    def rle(self, s):
        result = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(str(count) + s[i - 1])
                count = 1
        result.append(str(count) + s[-1])
        return ''.join(result)