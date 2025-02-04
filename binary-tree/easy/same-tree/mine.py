import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    """
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

    Solução: BFS
    """

    if p is None and q is None: return True
    elif p is None: return False
    elif q is None: return False

    queue = collections.deque()
    queue.append(p)
    queue.append(q)

    while queue:
        p_node = queue.popleft()
        if not p_node: return False

        q_node = queue.popleft()
        if not q_node: return False

        if p_node.val != q_node.val: return False

        if p_node.left or q_node.left: 
            queue.append(p_node.left)
            queue.append(q_node.left)

        if p_node.right or q_node.right: 
            queue.append(p_node.right)
            queue.append(q_node.right)
            
    return True