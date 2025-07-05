# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        d1=deque()
        d1.append((root.left,root.right))
        while d1:
            left,right=d1.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            d1.append((left.left,right.right))
            d1.append((left.right,right.left))
        return True
            