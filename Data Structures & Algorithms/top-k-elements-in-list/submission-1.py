class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        out = []
        for key, val in freq.items():
            buckets[val].append(key)
        for i in range(len(nums), 0, -1):
            k -= len(buckets[i])
            out += buckets[i]
            if k <= 0:
                break
        return out