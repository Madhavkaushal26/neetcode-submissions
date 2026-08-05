# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base Case: empty node / leaf child boundary
        if not root:
            return None
        
        # 1. Swap the left and right children directly on the node
        root.left, root.right = root.right, root.left
        
        # 2. Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 3. Return the inverted root
        return root