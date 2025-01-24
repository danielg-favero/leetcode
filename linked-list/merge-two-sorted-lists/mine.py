class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    """
    You are given the `heads` of two sorted linked lists `list1` and `list2`.

    Merge the two lists into one sorted list. 
    The list should be made by splicing together the nodes of the first two lists.

    Return the `head` of the merged linked list.
    """
    if not list1: return list2
    if not list2: return list1

    if list1.val <= list2.val:
        sorted_list = list1
        sorted_list.next = list2
        list1 = list1.next
    else:
        sorted_list = list2
        sorted_list.next = list1
        list2 = list2.next

