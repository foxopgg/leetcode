class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        result = 0
        sign = 1
        maxInt = 2 ** 31 - 1
        minInt = -2 ** 31

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        if result < minInt:
            return minInt
        if result > maxInt:
            return maxInt
        return result