# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    """
    Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

    Melhor solução: chegar na metade da lista, inverter da metade pra frente e comparar os valores em sequência
    """
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    previous = None
    current = slow.next

    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp

    while previous:
        if previous.val != head.val: return False
        previous = previous.next
        head = head.next

    return True