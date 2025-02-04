import collections

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(self, node: Node) -> Node:
    """
    Given a reference of a node in a `connected` undirected graph.

    Return a `deep copy` (clone) of the graph.

    Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.
    
    Solução: DFS
    """

    if not node: return node

    q = collections.deque([node])

    clones = {}
    clones[node.val] = Node(node.val, [])

    while q:
        current = q.popleft()
        current_clone = clones[current.val]

        for neighbor in current.neighbors:
            if neighbor.val not in clones: # Em um hasmap, essa operação é O(1)
                clones[neighbor.val] = Node(neighbor.val, [])
                q.append(neighbor)

            current_clone.neighbors.append(clones[neighbor.val])
            

    return clones[node.val]
