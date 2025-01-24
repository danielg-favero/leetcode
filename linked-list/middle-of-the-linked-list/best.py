class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: ListNode) -> ListNode:
    """
    Given the `head` of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.

    Solução: Fazer um ponteiro andar duas vezes mais rápido que outro
    """

    ahead = head

    while ahead and ahead.next:
        ahead = ahead.next.next
        head = head.next

    return head