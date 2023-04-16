# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        def iot(root):

            if root is not None:
                iot(root.left)
                result.append(root.val)
                iot(root.right)

            # return result

        iot(root)
        return result