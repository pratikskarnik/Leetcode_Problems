# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.array=[]
        self.postorder(root)
        return self.array
        
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.array.append(root.val)
            
        