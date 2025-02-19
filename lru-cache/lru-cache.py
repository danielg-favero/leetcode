class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LRUCache:
    """
    Design a data structure that follows the constraints of a `Least Recently Used (LRU) cache`.

    Implement the LRUCache class:

    - `LRUCache(int capacity)` Initialize the `LRU cache` with positive size capacity.
    - int `get(int key)` Return the value of the key if the key exists, otherwise return `-1`.
    - void `put(int key, int value)` Update the value of the key if the key exists. 
    Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds 
    the capacity from this operation, evict the least recently used key.

    The functions `get` and `put` must each run in `O(1)` average time complexity.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.previous = self.left

    def remove(self, node):
        _previous, _next = node.previous, node.next
        _previous.next = _next
        _next.previous = _previous

    def insert(self, node):
        _previous, _next = self.left, self.left.next
        _previous.next = _next.previous = node
        node.next = _next
        node.previous = _previous

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.right.previous
            self.remove(lru)
            del self.cache[lru.key]

obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
param_1 = obj.get(1)        
obj.put(3, 3)
param_1 = obj.get(2)
print(param_1)
