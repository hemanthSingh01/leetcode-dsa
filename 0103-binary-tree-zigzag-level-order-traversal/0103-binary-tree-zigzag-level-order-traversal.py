# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                return []
            queue = deque([root])
            result = []
            count = 0 
            while queue:
                level_size = len(queue)
                res = []
                for _ in range(level_size):
                    current = queue.popleft()
                    res.append(current.val)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                if count % 2 != 0:
                    res.reverse()
                result.append(res)
                count += 1  
            return result

        
