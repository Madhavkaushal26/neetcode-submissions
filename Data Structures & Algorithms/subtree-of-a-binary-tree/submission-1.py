# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def Pre_trav(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#,"

        stack = [root]
        res = ""

        while stack:
            curr = stack.pop()

            if curr is None:
                # Add null marker with a delimiter
                res += "#,"
            else:
                # Add node value with a comma delimiter (e.g., ",12,") to prevent value collisions
                res += f",{curr.val},"

                # Always push right then left, even if they are None
                stack.append(curr.right)
                stack.append(curr.left)

        return res

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        main = self.Pre_trav(root)
        sub = self.Pre_trav(subRoot)
        return sub in main

        