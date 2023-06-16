# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def get_height(node):
            if node is None:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        height_diff = abs(left_height - right_height)
        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)
        return height_diff <= 1 and left_balanced and right_balanced