class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    You are given the `heads` of two sorted linked lists `list1` and `list2`.

    Merge the two lists into one sorted list. 
    The list should be made by splicing together the nodes of the first two lists.

    Return the `head` of the merged linked list.
    """
    if not list1: return list2
    if not list2: return list1

    sorted_list = None
    sorted_head = None

    if list1.val <= list2.val:
        sorted_head = list1
        sorted_list = list1
        list1 = list1.next
    else:
        sorted_head = list2
        sorted_list = list2
        list2 = list2.next

    while list1 or list2:
        if list1 and list2:
            print(list1.val, list2.val)
            if list1.val <= list2.val:
                sorted_list.next = list1
                sorted_list = sorted_list.next
                list1 = list1.next
            else:
                sorted_list.next = list2
                sorted_list = sorted_list.next
                list2 = list2.next
        elif list1:
            sorted_list.next = list1
            sorted_list = sorted_list.next
            list1 = list1.next
        else:
            sorted_list.next = list2
            sorted_list = sorted_list.next
            list2 = list2.next

    sorted_list = sorted_head

    return sorted_list

a3 = ListNode(4, None)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)

b3 = ListNode(4, None)
b2 = ListNode(3, b3)
b1 = ListNode(1, b2)

print(mergeTwoLists(a1, b1))