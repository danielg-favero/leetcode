class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    """
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path 
    from the root node down to the farthest leaf node.

    Solução: DFS
    """
    if root is None: return 0

    left_height = maxDepth(root.left)
    right_height = maxDepth(root.right)

    return 1 + max(left_height,right_height)