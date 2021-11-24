from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        prev = head
        next = head.next
        if prev.val ==
        # if not temp1.next:
        #     return None
        while temp1:
            if temp1 == head and temp1.val == val:
                head = head.next
                temp1 = head
                continue
            elif temp1.next and temp1.next.val == val:
                temp = temp1.next.next
                temp1.next = temp
            # if temp1.next:
            temp1 = temp1.next
        return head

    def print_LL(self, head):
        while head:
            print(head.val)
            head = head.next


a = ListNode(7)
b = ListNode(2)
c = ListNode(2)
d = ListNode(1)
a.next = b
b.next =c
c.next =d
# a = ListNode(1)

abc = Solution()
print(abc.print_LL(abc.removeElements(a,2)))