class Solution(object):
    def intToRoman(self, num):
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanNumerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ""
        for i in range(len(integers)):
            while integers[i] <= num:
                num -= integers[i]
                result += romanNumerals[i]
            if num == 0:
                break
        return result