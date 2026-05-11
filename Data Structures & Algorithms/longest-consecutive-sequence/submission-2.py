class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        max_len = 1
        for n in nums:
            if n - 1 in nums_set:
                continue
            i = 1
            curr_len = 1
            while True:
                if n + i in nums_set:
                    curr_len += 1
                    i += 1
                else:
                    break
            max_len = max(max_len, curr_len)
        return max_len