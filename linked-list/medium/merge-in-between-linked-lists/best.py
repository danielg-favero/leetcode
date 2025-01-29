class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    """
    You are given two linked lists: `list1` and `list2` of sizes `n` and `m` respectively.
    Remove `list1`'s nodes from the `ath` node to the `bth` node, and put `list2` in their place.
    The blue edges and nodes in the following figure indicate the result:
    """
    remove_start = list1

    for _ in range(a):
        remove_start = remove_start.next

    remove_end = remove_start
    for _ in range(b - a + 1):
        remove_end = remove_end.next

    remove_end = remove_end.next
    remove_start.next = list2

    while list2.next:
        list2 = list2.next

    list2.next = remove_end

    return list1