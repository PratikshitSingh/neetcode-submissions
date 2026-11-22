# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if root and not subRoot: return False
        if not root and subRoot: return False

        if root.val == subRoot.val:
            if self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right):
                return True

        if self.isSubtree(root.left, subRoot): return True
        if self.isSubtree(root.right, subRoot): return True

        return False

