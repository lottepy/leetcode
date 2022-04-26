# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def depthTraversal(root: TreeNode, mark: str) -> List[int]:
            return depthTraversal(root.left, 'l') + depthTraversal(root.right, 'r') + [root.val] if root else [mark]
        return depthTraversal(p, 'r') == depthTraversal(q, 'r')  