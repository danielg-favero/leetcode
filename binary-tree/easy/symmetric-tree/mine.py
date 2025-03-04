class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    """
    Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

    Solução: Preorder traversal
    """
    left_result = []
    right_result = []

    def preorder_traversal(node: TreeNode, result: list):
        if node:
            result.append(node.val)
            preorder_traversal(node.left, result)
            preorder_traversal(node.right, result)
        else:
            result.append(-1)

    def reverse_preorder_traversal(node: TreeNode, result: list):
        if node:
            result.append(node.val)
            reverse_preorder_traversal(node.right, result)
            reverse_preorder_traversal(node.left, result)
        else:
            result.append(-1)

    preorder_traversal(root, left_result)
    reverse_preorder_traversal(root, right_result)

    return left_result == right_result