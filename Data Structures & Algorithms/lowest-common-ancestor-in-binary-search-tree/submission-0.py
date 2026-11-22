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
        minv, maxv = min(p.val,q.val), max(p.val,q.val)

        def LCA(root, minv, maxv):
            if minv < root.val and maxv < root.val:
                return LCA(root.left, minv, maxv)

            elif minv > root.val and maxv > root.val:
                return LCA(root.right, minv, maxv)

            else:
                return root
        
        return LCA(root, minv, maxv)