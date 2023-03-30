# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Sort of brutal solution
        #first_number = ""
        #second_number = ""
        #output = []

        #for i in l1[::-1]:
        #    first_number += str(i)

        #for j in l2[::-1]:
        #    second_number += str(j)

        #sum = str(int(first_number)+int(second_number))
        #for number in sum[::-1]:
        #    output.append(int(number))
        #return output

        # Popular solution
        #calc = rest = ListNode()
        #carry = 0
        #while l1 or l2:
        #    v1, v2 = 0, 0
        #    if l1:
        #        v1 = l1.val
        #        l1 = l1.next
        #    if l2:
        #        v2 = l2.val
        #        l2 = l2.next
        #    carry, val = divmod(v1+v2+carry, 10)
        #    rest.next = ListNode(val)
        #    rest = rest.next
        #if carry:
        #    rest.next = ListNode(carry)
        #return calc.next

        added = ListNode(val = (l1.val + l2.val) % 10)
        carry_over = (l1.val + l2.val) // 10
        current_node = added

        while(l1.next and l2.next):
            l1 = l1.next
            l2 = l2.next
            current_node.next = ListNode(val = (carry_over + l1.val + l2.val) % 10)
            carry_over = (carry_over + l1.val + l2.val) // 10
            current_node = current_node.next

        while(l1.next):
            l1 = l1.next
            current_node.next = ListNode(val = (carry_over + l1.val) % 10)
            carry_over = (carry_over + l1.val) // 10
            current_node = current_node.next
        while(l1.next):
            l2 = l2.next
            current_node.next = ListNode(val = (carry_over + l2.val) % 10)
            carry_over = (carry_over + l2.val) // 10
            current_node = current_node.next

        if carry_over > 0:
            current_node.next = ListNode(val = 1)

        return added