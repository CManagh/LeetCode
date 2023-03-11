from math import *


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        merged = nums1 + nums2
        output = sorted(merged)
        leng = len(output)
        temp = leng+1
        mid = temp/2
        if float(floor(mid)) == mid:
            return output[int(mid)-1]
        else:
            floorm = floor(mid)
            roof = ceil(mid)
            b = output[floorm-1]
            a = output[roof-1]
            return (a+b)/2



nums1 = [1,3]
nums2 = [2]
obj = Solution()
returnVal = obj.findMedianSortedArrays(nums1, nums2)
print(returnVal)
# 2 3 3 4 4 5 5 32