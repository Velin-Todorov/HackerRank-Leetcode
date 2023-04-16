# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        resut = 0

        def rec_sum(root):

            nonlocal resut

            if root:

                rec_sum(root.left)
                
                if root.val in range(low, high + 1):
                    resut += root.val
            
                rec_sum(root.right)
        
        rec_sum(root)

        return resut


