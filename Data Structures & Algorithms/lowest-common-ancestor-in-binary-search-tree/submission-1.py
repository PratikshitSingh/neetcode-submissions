# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        p, q > root => LCA(root.right)
        p, q < root => LCA(root.left)
        p < root < q => root
        """

        def LCA(root):
            if p.val < root.val and q.val < root.val:
                return LCA(root.left)

            elif p.val > root.val and q.val > root.val:
                return LCA(root.right)

            else:
                return root
        
        return LCA(root)