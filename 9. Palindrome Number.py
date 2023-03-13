class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        print(x)
        if x < 0:
            return False
        else:
            return int(str(x)[::-1]) == x


input = 121
obj = Solution()
returnVal = obj.isPalindrome(input)
print(returnVal)
