class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: Node) -> Node:
    """
    A linked list of length `n` is given such that each node contains an additional random pointer, 
    which could point to any node in the list, or `null`.

    Construct a deep copy of the list. The deep copy should consist of exactly `n` brand new nodes, 
    where each new node has its value set to the value of its corresponding original node. 
    Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list 
    such that the pointers in the original list and copied list represent the same list state. 
    None of the pointers in the new list should point to nodes in the original list.

    For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, 
    then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

    Return the head of the copied linked list.

    The linked list is represented in the input/output as a list of `n` nodes. 
    Each node is represented as a pair of `[val, random_index]` where:
    - `val`: an integer representing `Node.val`
    - `random_index`: the index of the node (range from `0` to `n-1`) that the random pointer points to, 
    or `null` if it does not point to any node.

    Your code will only be given the `head` of the original linked list.
    """
    hash_map = {}
    current = head
    
    while current is not None:
        # Cria-se um novo Node com base no atual
        hash_map[current] = Node(current.val)
        current = current.next

    current = head

    while current is not None:
        new_node = hash_map.get(current)
        new_node.next = hash_map.get(current.next)
        new_node.random = hash_map.get(current.random)

        current = current.next

    return hash_map.get(head)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.random = head.next.next
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head.next

copyRandomList(head)