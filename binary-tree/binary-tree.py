from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, value, node: TreeNode):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(value, node.left)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(value, node.right)

    def search(self, value):
        return self._search_recursive(value, self.root)
    
    def _search_recursive(self, value, node: TreeNode):
        if not node: return False
        if value == node.value: return True
        elif value < node.value: return self._search_recursive(value, node.left)
        else: return self._search_recursive(value, node.right)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result
    
    def _preorder_traversal(self, node: TreeNode, result: list):
        if node:
            result.append(node.value)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, node: TreeNode, result: list):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result
    
    def _postorder_traversal(self, node: TreeNode, result: list):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.value)

    def bfs(self, value: int):
        if self.root is None: return False

        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()

            if node.value == value: return True

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        return False
    
    # Mesma coisa que um Preorder Traversal
    def dfs(self, value: int): 
        return self._dfs(self.root, value)

    def _dfs(self, node: TreeNode, value: int): 
        if node is None: return False
        if node.value == value: return True

        if self._dfs(node.left, value): return True
        if self._dfs(node.right, value): return True
