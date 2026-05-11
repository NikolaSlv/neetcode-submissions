class Solution:
    def anagram(self, s1: str, s2: str) -> bool:
        freq = [0] * 26
        base = ord('a')
        for ch in s1:
            freq[ord(ch) - base] += 1
        for ch in s2:
            freq[ord(ch) - base] -= 1
            if freq[ord(ch) - base] < 0:
                return False
        for i in range(26):
            if freq[i] > 0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        proc = set()
        for i in range(len(strs)):
            if strs[i] in proc:
                continue
            newGroup = [strs[i]]
            proc.add(strs[i])
            for j in range(i + 1, len(strs)):
                if self.anagram(strs[i], strs[j]):
                    newGroup.append(strs[j])
                    proc.add(strs[j])
            groups.append(newGroup)
        return groups