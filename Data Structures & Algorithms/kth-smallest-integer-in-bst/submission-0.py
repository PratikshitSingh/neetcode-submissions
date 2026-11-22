# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        1. do preorder traversal DFS and count till k.

        T: O(K)
        S: O(K)
        """
        count = 0
        answer = 0

        def dfs(root):
            if not root: return

            dfs(root.left)
            
            nonlocal count
            nonlocal answer
            count += 1
            if count == k:
                answer = root.val

            dfs(root.right)

        dfs(root)
        return answer