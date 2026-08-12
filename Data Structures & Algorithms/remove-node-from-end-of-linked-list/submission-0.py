# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        curr = head
        while curr.next is not None:
            length += 1
            curr = curr.next

        dummy = ListNode(0, head)
        curr = dummy
        steps = length - n
        for _ in range(steps):
            curr = curr.next

        curr.next = curr.next.next
        return dummy.next
            


        