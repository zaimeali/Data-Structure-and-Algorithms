# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = None
        nums = sorted(nums)
        size = len(nums)
        for i in range(0, size - 1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]

        return nums[-1]
