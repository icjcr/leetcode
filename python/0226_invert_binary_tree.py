from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree_recursively(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root

    root.left, root.right = root.right, root.left
    invert_tree_recursively(root.left)
    invert_tree_recursively(root.right)

    return root


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return root
