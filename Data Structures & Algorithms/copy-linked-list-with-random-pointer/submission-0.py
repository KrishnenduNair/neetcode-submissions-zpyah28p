"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        change = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            change[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = change[curr]
            copy.next = change[curr.next]
            copy.random = change[curr.random]
            curr = curr.next

        return change[head]



        