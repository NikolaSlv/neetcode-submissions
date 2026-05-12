class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        print(nums)
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == -nums[i]:
                    out.append([nums[left], nums[right], nums[i]])
                    prev_left, prev_right = left, right
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[prev_left]:
                        left += 1
                    while left < right and nums[right] == nums[prev_right]:
                        right -= 1
                elif two_sum < -nums[i]:
                    left += 1
                else:
                    right -= 1
        return out