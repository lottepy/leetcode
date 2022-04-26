# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorderTraversal(root: TreeNode, mark: str) -> List[int]:
            return inorderTraversal(root.left, 'l') + inorderTraversal(root.right, 'r') + [root.val] if root else [mark]
        return inorderTraversal(p, 'r') == inorderTraversal(q, 'r')  