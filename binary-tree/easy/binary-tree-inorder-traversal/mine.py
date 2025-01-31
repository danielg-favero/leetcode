
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode) -> list[int]:
    """
    Given the `root` of a binary tree, return the inorder traversal of its nodes' values.
    """
    
    def inorder(root: TreeNode):
        return inorder(root.left) + [root.val] + inorder(root.right) if root else []

    return inorder(root)
        