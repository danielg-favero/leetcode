class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        """
        Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal 
        of a binary tree and `postorder` is the postorder traversal of the same tree, 
        construct and return the binary tree.

        Solução:
        - No `postorder` o último elemento do array é o root da árvore
        - No `inorder` os elementos a esquerda do root estão a esquerda do array e 
            os elementos a direita do root estão a direita do array
        """
        
        if not inorder or not postorder: return None
        
        def construct(_inorder: list[int], _postorder: list[int]) -> TreeNode:
            if not len(_postorder) or not len(_inorder): return None        
            root = TreeNode(postorder.pop())

            root_inorder_index = _inorder.index(root.val)
            # Isso é ineficiente por que estamos criando novos arrays, isso não precisaria
            left_inorder = _inorder[:root_inorder_index]
            right_inorder = _inorder[root_inorder_index+1:]
        
            root.right = construct(right_inorder, _postorder)
            root.left = construct(left_inorder, _postorder)
        
            return root
    
        return construct(inorder, postorder)