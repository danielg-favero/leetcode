import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(self, root: TreeNode) -> list[list[int]]:
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values. 
    (i.e., from left to right, level by level).

    Solução: BFS
    """

    if root is None: return []

    result = []

    queue = collections.deque()
    queue.append(root)

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left: 
                queue.append(node.left)

            if node.right: 
                queue.append(node.right)
        
        if level:
            result.append(level)

    return result