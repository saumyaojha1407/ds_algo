class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list(object):
    def __init__(self):
        self.head = None

head = Node(1)
item1 = Node(2)
head.next = item1
item2 = Node(3)
item1.next = item2

item3 = Node(4)
item2.next = item3

iterate = head
temp1 = head
temp2 = None

# temp = head
# while(temp != None):
#     print(temp.data)
#     temp = temp.next


while(iterate != None):
    temp1 = iterate.next
    # if iterate == head:
    #     iterate.next = None
    # else:
    iterate.next = temp2
    temp2 = iterate
    iterate = temp1

head = temp2

temp = head
while(temp != None):
    print(temp.data)
    temp = temp.next