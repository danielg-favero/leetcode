class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTilt(root: TreeNode) -> int:
    """
    Given the `root` of a binary tree, return the sum of every tree node's tilt.

    The tilt of a tree node is the absolute difference between the sum of all left subtree node values
    and all right subtree node values. If a node does not have a left child, then the sum of the left
    subtree node values is treated as `0`. The rule is similar if the node does not have a right child.
    """
    
    def sum(node): 
        if node is None: return 0

        left_sum = 0
        right_sum = 0
        if node.left:
            left_sum += sum(node.left)
        if node.right:
            right_sum += sum(node.right)

        return node.val + left_sum + right_sum

    def tilt(node):
        if node is None: return 0

        left = tilt(node.left)
        right = tilt(node.right)

        return abs(sum(node.left) - sum(node.right)) + left + right

    return tilt(root)