# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.inorderTraversal(p,q)
        
    def inorderTraversal(self,p,q):
        if p and q:
            if p.val!=q.val:
                return False
            return self.inorderTraversal(p.left,q.left) and self.inorderTraversal(p.right,q.right)
        elif p or q:
            return False
        else:
            return True
        
        