class Solution(object):
    def generateParenthesis(self, n):
        def generate(openP, closeP, brackets):
            if openP == closeP == n:
                ans.append(brackets)
            if openP < n:
                generate(openP + 1, closeP, brackets + "(")
            if closeP < openP:
                generate(openP, closeP + 1, brackets + ")")
        ans = []
        generate(0, 0, "")
        return ans