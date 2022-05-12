# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals=[]
        while head:
            vals.append(head.val)
            head=head.next
        return self.constructTree(vals)
        
        
    def constructTree(self,vals):
        if vals:
            mid = len(vals)//2
            root=TreeNode(vals[mid])
            root.left=self.constructTree(vals[:mid])
            root.right=self.constructTree(vals[mid+1:])
            return root
        
        