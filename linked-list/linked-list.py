class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def shift(self, value):
        node = Node(value)
        node.next = self.head

        if self.head:
            self.head.previous = node
        else:
            self.tail = node

        self.head = node
    
    def push(self, value):
        node = Node(value)
        node.previous = self.tail

        if self.tail:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node

    def unshift(self) -> Node:
        if not self.head:
            return None
        
        removed_node = self.head
        self.head = self.head.next
        
        if self.head:
            self.head.previous = None
        else:
            self.tail = None

        return removed_node
    
    def pop(self) -> Node:
        if not self.tail:
            return None
        
        removed_node = self.tail
        self.tail = self.tail.previous
        
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        return removed_node