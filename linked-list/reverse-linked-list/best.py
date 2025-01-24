class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    """
    Given the `head` of a singly linked list, reverse the list, and return the reversed list.
    """

    new_head = None

    while head:
        next_node = head.next
        head.next = new_head
        new_head = head
        head = next_node

    return new_head