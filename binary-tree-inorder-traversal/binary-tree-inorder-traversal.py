# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.array=[]
        self.inorder(root)
        return self.array
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.array.append(root.val)
            self.inorder(root.right)

        