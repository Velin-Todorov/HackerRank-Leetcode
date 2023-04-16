class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        dl = []
        max_d = 0

        def iot(root, depth):
            nonlocal dl, max_d

            if root:
                
                if root.left is None and root.right is None:

                    if depth > max_d:
                        max_d = depth
                        dl = [root.val]
                    
                    elif depth == max_d:
                        dl.append(root.val)

                    # total_sum += root.val
                else:
                    iot(root.left, depth + 1)
                    iot(root.right, depth + 1)

        iot(root, 0)
        return sum(dl)
            