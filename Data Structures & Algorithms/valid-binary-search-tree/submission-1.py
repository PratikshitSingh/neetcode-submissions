# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        keep range [-inf, inf]
        check r.l < r < r.r 
        isValidBST(r.l) and isValidBST(r.r)

        T: O(N)
        S: O(N)
        """
        mini, maxi = float("-inf"), float("inf")

        def validate(root, mini, maxi):
            if root:
                root_check = (root.val > root.left.val if root.left else True) and (root.val < root.right.val if root.right else True)
                root_check = root_check and (mini < root.val < maxi)

                return root_check and validate(root.left, mini, root.val) and validate(root.right, root.val, maxi)
            
            return True

        return validate(root, mini, maxi)