class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
def find_middle(head: Node):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(l1: Node, l2: Node):
    head = Node()
    tail = head

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2

    return head.next 

def merge_sort(head: Node):
    """
    Complexidade temporal:
    - Sempre: `O(nlogn)`

    Complexidade espacial: 
    - Sempre: O(n)
    """

    if not head or not head.next:
        return head

    middle = find_middle(head)
    after_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(after_middle)

    sorted_list = merge(left, right)

    return sorted_list

node_1 = Node(7)
node_2 = Node(2, next=node_1)
node_3 = Node(6, next=node_2)
node_4 = Node(3, next=node_3)

merge_sort(node_4)