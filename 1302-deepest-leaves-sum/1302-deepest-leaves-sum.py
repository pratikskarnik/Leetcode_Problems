# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue=[(1,root)]
        max_depth=1
        result=0
        while(len(queue)>0):
            depth,node=queue.pop(0)
            if depth>max_depth:
                max_depth=depth
                result=node.val
            elif depth==max_depth:
                result+=node.val
                
            if node.left:
                queue.append((depth+1,node.left))
            if node.right:
                queue.append((depth+1,node.right))
        return result
        
        