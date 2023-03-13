class Solution(object):
    MAX = 2 ** 31 - 1
    MIN = -2 ** 31

    def reverse(self, x: int):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            var = int(str(x)[1:][::-1])
            return self.checkSize(var * -1)
        else:
            return self.checkSize(int(str(x)[::-1]))

    def checkSize(self, val):
        if val > self.MAX:
            return 0
        elif val < self.MIN:
            return 0
        else:
            return val


input = -32
obj = Solution()
returnVal = obj.reverse(32)
print(returnVal)
