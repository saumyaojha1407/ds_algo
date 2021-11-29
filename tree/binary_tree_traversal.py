from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return  self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)



if __name__ == '__main__':
    root = TreeNode(1)
    A = TreeNode(2)
    B = TreeNode(3)
    root.right = A
    A.left = B
    obj = Solution()
    preorder = obj.preorderTraversal(root)
    postorder = obj.postorderTraversal(root)
    inorder = obj.inorderTraversal(root)

    print(preorder)
    print(postorder)
    print(inorder)
