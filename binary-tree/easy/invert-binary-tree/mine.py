
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    """
    Given the `root` of a binary tree, invert the tree, and return its root.
    """
    def invert(node):
        if node is None: return None

        node.left, node.right = node.right, node.left

        invert(node.left)
        invert(node.right)

        return node
        
    return invert(root)