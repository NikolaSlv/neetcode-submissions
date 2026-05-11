class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_dict = defaultdict(list)
        for i in range(len(nums)):
            nums_dict[nums[i]].append(i)
        
        out_set = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                two_sum = nums[i] + nums[j]
                if 0 - two_sum in nums_dict:
                    for idx in nums_dict[0 - two_sum]:
                        if idx != i and idx != j:
                            out_set.add(tuple(sorted([nums[i], nums[j], nums[idx]])))
        
        out = []
        for t in out_set:
            out.append(list(t))
        return out