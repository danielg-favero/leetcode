# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    """
    Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
    """
    if not head: return False
    if not head.next: return True

    last = head.next

    while head != last:
        before_last = head
        while before_last.next.next:
            before_last = before_last.next
        last = before_last.next

        if head.val != last.val: return False

        if head == before_last:
                return True
        last = before_last
        before_last.next = None
        head = head.next

    return True

node_1 = ListNode(1)
node_2 = ListNode(2, next=node_1)
node_3 = ListNode(2, next=node_2)
node_4 = ListNode(1, next=node_3)
isPalindrome(node_4)

node_1 = ListNode(2)
node_2 = ListNode(1, next=node_1)
isPalindrome(node_2)