class Solution:
    def getSigArr(self, s: str) -> tuple:
        freq = [0] * 26
        base = ord('a')
        for ch in s:
            freq[ord(ch) - base] += 1
        return tuple(freq)

    def getSigSort(self, s: str) -> tuple:
        return tuple(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            sig = self.getSigSort(s)
            groups[sig].append(s)
        return list(groups.values())