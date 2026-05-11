class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(len(nums)):
            prefix.append(prefix[i] * nums[i])
        suffix = [1] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i + 1])
        return output