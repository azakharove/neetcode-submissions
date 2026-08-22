# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root is None:
        #     return None
        # original_root = root
        # queue = [root]
        # while queue:
        #     root = queue.pop()
        #     left = root.left
        #     right = root.right
        #     root.left = right
        #     root.right = left
        #     if root.left:
        #         queue.append(root.left)
        #     if root.right:
        #         queue.append(root.right)
        # return original_root
        if root is None:
            return None

        left = root.left
        right = root.right
        root.left = right
        root.right = left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
            

