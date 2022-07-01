# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head=head.next
        result=0
        head3=ListNode()
        head2=head3
        while head:
            if head.val!=0:
                result+=head.val
            else:
                head2.next=ListNode(result)
                head2=head2.next
                result=0
            head=head.next
        return head3.next
                
        