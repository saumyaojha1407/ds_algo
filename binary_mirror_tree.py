class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, head):
        self.head = head

    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.data, end = " ")
        self.inorder(node.right)

    def mirror(self, node):
        if not node:
            return
        temp1 = node.left
        temp2 = node.right
        self.mirror(node.left)
        self.mirror(node.right)
        node.left = temp2
        node.right = temp1


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    binary = BinaryTree(root)
    binary.inorder(root)
    binary.mirror(root)
    binary.inorder(root)