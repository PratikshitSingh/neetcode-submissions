# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        bfs_results = []

        if root:
            queue.append(root)

        while queue:
            s = len(queue)
            level_results = []

            while s:
                node = queue.popleft()
                level_results.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                s -= 1
            bfs_results.append(level_results)
        
        return bfs_results