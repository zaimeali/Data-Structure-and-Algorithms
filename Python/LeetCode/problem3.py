# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myIntersect = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                removeIndex = nums2.index(nums1[i])
                a = nums2.pop(removeIndex)
                myIntersect.append(a)

        return myIntersect
