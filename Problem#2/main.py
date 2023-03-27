# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_number = ""
        second_number = ""
        output = []

        for i in l1[::-1]:
            first_number += str(i)

        for j in l2[::-1]:
            second_number += str(j)

        sum = str(int(first_number)+int(second_number))
        for number in sum[::-1]:
            output.append(int(number))

        return output