# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mySet = set()
        myIndex = list()
        for i in range(len(nums)):
            if nums[i] in mySet:
                myIndex.append(i)
            else:
                mySet.add(nums[i])
        for i in reversed(myIndex):
            nums.pop(i)
        return len(mySet)
