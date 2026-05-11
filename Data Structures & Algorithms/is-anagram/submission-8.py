class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        base = ord('a')
        for ch in s:
            freq[ord(ch) - base] += 1
        for ch in t:
            freq[ord(ch) - base] -= 1
            if freq[ord(ch) - base] < 0:
                return False
        for i in range(26):
            if freq[i] > 0:
                return False
        return True