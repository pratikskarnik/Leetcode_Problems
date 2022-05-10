# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        head2=head
        while head:
            head=head.next
            i+=1
        i=i-n
        n=0
        head3=head2
        if i==0:
            return head3.next
        while head2:
            n+=1
            if n==i:
                head2.next=head2.next.next
            head2=head2.next
        return head3
            
            
        