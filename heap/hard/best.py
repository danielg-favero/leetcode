import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[ListNode]) -> ListNode:
    """
    You are given an array of `k` linked-lists `lists`, 
    each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list 
    and return it.

    Soluções: Merge Sort, Brute Force, Heap
    """

    heap = []

    def push_node(heap, node):
        if node:
            # O heap sempre ordena pelo primeiro elemento da tupla, depois pelo segundo e etc.
            heapq.heappush(heap, (node.val, id(node), node))

    # Armazenando os heads das listas em um heap
    for heads in lists:
        push_node(heap, heads)

    # Os resultados serão armazenados em uma lista
    result = ListNode()
    current = result

    while heap:
        _, _, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        # Verifica se ainda há elementos para serem adicionados no heap
        # Quando adicionados novos elementos no heap, há a garantia que o menor valor está na primeira posição
        if node.next:
            push_node(heap, node.next)