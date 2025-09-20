class Solution(object):
    def romanToInt(self, s):
        intToRom = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        previous = 0
        result = 0
        for char in reversed(s):
            current = intToRom[char]
            if current < previous:
                result -= current
            else:
                result += current
            previous = current
        return result