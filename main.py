from typing import Type


class Solution(object):
    def twoSum(self, nums, target):
        """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
                """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


temparray = [2, 3, 3,4,4,6,2]
target = 6
obj = Solution()
returnVal = obj.twoSum(temparray, target)
print(returnVal)