class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        result = ""
        strs.sort(key=len)
        for i in range(0, len(strs[0])):
            result = strs[0][0:i+1]
            for k in range(0, len(strs) - 1):
                if result == strs[k+1][0:i+1]:
                    continue
                else:
                    return result[0:len(result)-1]
        return result