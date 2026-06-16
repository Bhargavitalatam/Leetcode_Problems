# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        fi=dummy
        se=dummy
        for i in range(n+1):
            fi=fi.next
        while fi is not None:
            fi=fi.next
            se=se.next
        se.next=se.next.next
        return dummy.next

        