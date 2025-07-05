# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        depth = 0
        if root:
            queue.append(root)

        while queue:
            level_size = len(queue)  
            for _ in range(level_size):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            depth += 1
        return depth