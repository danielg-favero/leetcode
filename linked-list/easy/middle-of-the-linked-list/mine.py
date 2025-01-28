class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: ListNode) -> ListNode:
    """
    Given the `head` of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.
    """

    current_node = head
    counter = 0

    while current_node:
        current_node = current_node.next
        counter +=1

    current_node = head
    for i in range(0, counter // 2):
        current_node = current_node.next

    return current_node