class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        i = 0
        while i < len(s):
            if i == len(t) or s[i] != t[i]:
                return False
            i += 1
        if i < len(t):
            return False
        return True