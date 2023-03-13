class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list=[]
        if l1.size == l2.size:
            for num1,num2 in zip(l1,l2):
                list.append(num1+num2)
            return list[::-1]
        else:
            length1 = len(l1)
            length2 = len(l2)
            return l1 + l2