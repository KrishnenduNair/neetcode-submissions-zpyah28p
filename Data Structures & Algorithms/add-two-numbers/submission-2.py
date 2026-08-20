# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        carry = 0
        prev = None

        while curr1 or curr2:
            val = carry
            if curr1:
                val += curr1.val
            if curr2:
                val += curr2.val

            carry = val // 10
            val %= 10

            if curr1:
                curr1.val = val
                prev = curr1
                curr1 = curr1.next
                if curr2:
                    curr2 = curr2.next

            else:
                prev.next = curr2
                curr1 = curr2
                curr1.val = val
                prev = curr1
                curr1 = curr1.next
                curr2 = curr2.next

        if carry != 0:
            new = ListNode()
            new.val = carry
            prev.next = new
        
        return l1


        