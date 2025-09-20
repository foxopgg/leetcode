class Solution(object):
    def reverse(self, x):
	#Test
        result = 0
        sign = 1 if x > 0 else -1
        x = x * sign
        while x > 0:
            result = result * 10 + (x % 10)
            x = x // 10
            if result > 2**31 - 1:
                return 0
        return result * sign
