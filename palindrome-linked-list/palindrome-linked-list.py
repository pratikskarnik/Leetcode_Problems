# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slowNode = head
        fastNode = head
        while fastNode is not None and fastNode.next is not None:
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        reversedSecondHalfNode = self.reverseLinedList(slowNode)
        firstHalfNode = head

        while reversedSecondHalfNode:
            if reversedSecondHalfNode.val != firstHalfNode.val:
                return False
            reversedSecondHalfNode = reversedSecondHalfNode.next
            firstHalfNode = firstHalfNode.next

        return True
        
    def reverseLinedList(self,head):
        previous, current = None, head
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        return previous

        