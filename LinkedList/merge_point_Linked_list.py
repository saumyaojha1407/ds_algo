class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_merge_point(head1, head2):

    temp1 = head1
    temp2 = head2
    l1 = 0
    l2 = 0
    while temp1:
        l1 += 1
        temp1 = temp1.next
    while temp2:
        l2 += 1
        temp2 = temp2.next
    if l1 > l2:
        temp1 = head1
        temp2 = head2
        for _ in range(l1 - l2):
            temp1 = temp1.next
    else:
        temp1 = head1
        temp2 = head2
        for _ in range(l2 - l1):
            temp2 = temp2.next

    while temp1 and temp2:
        if temp1 == temp2:
            return temp1.data
        temp1 = temp1.next
        temp2 = temp2.next

    return -1


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e

p = Node(4)
q = Node(5)
p.next = q

print(get_merge_point(a, p))
