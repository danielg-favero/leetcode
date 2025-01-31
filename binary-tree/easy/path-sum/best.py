class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    """
    Given the `root` of a binary tree and an integer `targetSum`, 
    return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.
    A leaf is a node with no children.
    """
    if not root: return False
    if not root.right and not root.left and targetSum - root.val == 0: return True

    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)