from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        parents = [root]
        children = []
        out = []
        level = []
        while parents:
            parent = parents.pop(0)
            if parent.left:
                children.append(parent.left)
            if parent.right:
                children.append(parent.right)
            level.append(parent.val)
            if len(parents) == 0:
                parents = children
                children = []
                out.append(level)
                level = []
        return out



if __name__ == '__main__':
    root = TreeNode(1)
    A = TreeNode(2)
    B = TreeNode(3)
    root.right = A
    A.left = B
    obj = Solution()
    preorder = obj.levelorderTraversal(root)
    print(preorder)
