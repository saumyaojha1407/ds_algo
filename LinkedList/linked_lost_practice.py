class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        tmp = self.head
        count = 0
        while tmp:
            if index == count:
                return tmp.val
            tmp = tmp.next
            count +=1
        return -1

    def addAtHead(self, val: int) -> None:
        curr = ListNode(val)
        if not self.head:
            self.head = curr
        else:
            curr.next = self.head
            self.head = curr

    def addAtTail(self, val: int) -> None:
        curr = ListNode(val)
        tmp = self.head
        if not tmp:
            self.head = curr
        else:
            while tmp.next:
                tmp = tmp.next
            tmp.next = curr

    def addAtIndex(self, index: int, val: int) -> None:
        curr = ListNode(val)
        index_value = self.get(index)
        if index == 0:
            self.addAtHead(val)
        elif index_value == -1:
            self.addAtTail(val)
        else:
            count = 0
            prev = self.head
            tmp = prev.next
            while tmp:
                if count == index - 1:
                    curr.next = tmp
                    prev.next = curr
                    return
                prev = tmp
                tmp = tmp.next

    def deleteAtIndex(self, index: int) -> None:
        tmp = self.head
        if self.head:
            if index == 0:
                self.head = tmp.next
            else:
                tmp = self.head
                for i in range(0, index):
                    prev = tmp
                    if not tmp.next:
                        return
                    tmp = tmp.next
                if prev:
                    prev.next = tmp.next

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtIndex(3,0)
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
param_2 = obj.get(4)
obj.addAtHead(4)
obj.addAtIndex(5,0)
obj.addAtHead(6)
# print(param_1)
print(param_2)