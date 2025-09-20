class Solution(object):
    def isValid(self, s):
        paranthesesMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []
        for i in s:
            if i in paranthesesMap.values():
                stack.append(i)
            else:
                if not stack or stack.pop() != paranthesesMap[i]:
                    return False
        return not stack