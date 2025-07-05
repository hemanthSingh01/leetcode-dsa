# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        d1=deque()
        d2=deque()
        d1.append(p)
        d2.append(q)
        while d1 and d2:
            current1=d1.popleft()
            current2=d2.popleft()
            if not current1 and not current2:
                continue
            if not current1 or not current2:
                return False
            if current1.val!=current2.val:
                return False
            d1.append(current1.left)
            d1.append(current1.right)
            d2.append(current2.left)
            d2.append(current2.right)
        return True

