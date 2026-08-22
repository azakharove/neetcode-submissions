# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # maxd = 0
        # if root is None:
        #     return maxd
        # queue = [root]
        # while queue:
        #     curr = queue.pop()
        #     if curr.left is None and curr.right is None:
        #         continue
        #     if curr.left:
        #         queue.append(curr.left)
        #     if curr.right:
        #         queue.append(curr.right)
        #     maxd += 1
        # return maxd
        if root is None:
            return 0
        elif root.left or root.right:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 1


