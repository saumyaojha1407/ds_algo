from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def checkSymmetricity(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        parents = [root]
        children = []
        while parents:
            parent = parents.pop(0)
            if not parent:
                continue
            # if parent.left:
            children.append(parent.left)
            # if parent.right:
            children.append(parent.right)
            if len(parents) == 0:
                left = 0
                right = len(children) - 1
                while left < right:
                    if not (children[left]) and not (children[right]):
                        left += 1
                        right -= 1
                        continue
                    elif (not children[left] and children[right]) or (not children[right] and children[left]):
                        return False
                    elif children[left].val != children[right].val:
                        return False
                    left += 1
                    right -= 1
                parents = children
                children = []
        return True



if __name__ == '__main__':
    root = TreeNode(1)
    A = TreeNode(2)
    B = TreeNode(2)
    E = TreeNode(3)
    F = TreeNode(3)

    root.right = A
    root.left = B
    A.right = E
    B.right = F
    obj = Solution()
    preorder = obj.checkSymmetricity(root)
    print(preorder)
