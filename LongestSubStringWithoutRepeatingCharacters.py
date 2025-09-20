class Solution(object):
    def lengthOfLongestSubstring(self, s):
        characterSet = set()
        maxLength = left = right = 0
        for right in range(len(s)):
            while s[right] in characterSet:
                characterSet.remove(s[left])
                left += 1
            
            characterSet.add(s[right])
            maxLength = max (maxLength, right - left + 1)
        return maxLength