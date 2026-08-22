# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.left or root.right:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, self.maxDepth(root.left) + self.maxDepth(root.right))]
        global_max = 0
        while q:
            curr, maxi = q.pop()
            if maxi > global_max:
                global_max = maxi
            if curr.left:
                q.append((curr.left, self.maxDepth(curr.left.left) + self.maxDepth(curr.left.right)))
            if curr.right:
                q.append((curr.right, self.maxDepth(curr.right.left) + self.maxDepth(curr.right.right)))
        return global_max
