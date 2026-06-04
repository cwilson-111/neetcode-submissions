# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #check to see if there is a root node, if not 0
        if not root:
            return 0
        #check to see if root node has any children to left or right, if not return 1
        if not root.left and not root.right:
            return 1

        #find the max depth of either side of the root, else 0
        max_left = self.maxDepth(root.left) if root else 0
        max_right = self.maxDepth(root.right) if root else 0

        #return max between the two
        return max(max_left,max_right) + 1

        #faster approach is a single line which combines everything
        #return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        