# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        head = None
        while l1 and l2:
            if not head:
                if l1.val > l2.val:
                    head = l2
                    l2 = l2.next
                else:
                    head = l1
                    l1 = l1.next
                temp = head
            else:
                if l1.val > l2.val:
                    temp.next = l2
                    l2 = l2.next
                else:
                    temp.next = l1
                    l1 = l1.next
                temp = temp.next
        while l1:
            temp.next = l1
            l1 = l1.next
            temp = temp.next
        while l2:
            temp.next = l2
            l2 = l2.next
            temp = temp.next
        return head


    def print_LL(self, head):
        while head:
            print(head.val)
            head = head.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
a.next = b
b.next =c

p = ListNode(1)
q = ListNode(3)
r = ListNode(4)
p.next=q
q.next=r

abc = Solution()
print(abc.print_LL(abc.mergeTwoLists(a,p)))