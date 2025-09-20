class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 1:
            return dividend
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        a = -dividend if dividend > 0 else dividend
        b = -divisor if divisor > 0 else divisor
        ans = 0
        while a <= b:
            x = b
            cnt = 1
            while x >= -(2 ** 30) and a <= (x << 1):
                x <<= 1
                cnt <<= 1
            a -= x
            ans += cnt
        return ans if sign else -ans