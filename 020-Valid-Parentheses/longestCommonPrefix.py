class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {"(": ")", "{": "}", "[": "]"}
        open_par = ["(", "{", "["]
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and brackets_map[stack[-1]] == i:
                stack.pop()
            else:
                return False
        return stack == []