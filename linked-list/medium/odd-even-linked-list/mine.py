class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head: ListNode) -> ListNode:
    if not head.next: return head
    if not head.next.next: return head

    odds = head

    evens = head.next
    first_even = head.next

    while odds.next and evens.next:
        odds.next = evens.next
        odds = evens.next

        evens.next = odds.next
        evens = odds.next

    # Os índices pares sucedem os ímpares, por isso fazer apontar para o primeiro par
    odds.next = first_even

    return head

node_1 = ListNode(5)
node_2 = ListNode(4, node_1)
node_3 = ListNode(3, node_2)
node_4 = ListNode(2, node_3)
node_5 = ListNode(1, node_4)

oddEvenList(node_5)
