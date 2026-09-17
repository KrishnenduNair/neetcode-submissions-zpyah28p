# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dictionary = {}  # level -> list of values
        stack = [(root, 0)]

        while stack:
            node, lvl = stack.pop()

            if lvl not in dictionary:
                dictionary[lvl] = []
            dictionary[lvl].append(node.val)

            if node.left:
                stack.append((node.right, lvl + 1))
            if node.right:
                stack.append((node.left, lvl + 1))

        res = [dictionary[lvl] for lvl in sorted(dictionary)]
        return res

            
            
            
            
            