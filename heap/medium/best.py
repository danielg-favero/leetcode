import heapq
from typing import Counter

def topKFrequent(nums: list[int], k: int) -> list[int]:
    """
    Given an integer array `nums` and an integer `k`, 
    return the `k` most frequent elements. 

    You may return the answer in any order.
    """

    # Contar quantas vezes cada elementos repete no array
    quantities = Counter(nums)

     # Armazenar os elementos em uma heap, adicionando ele de forma negativa, assim o "Menor" valor estará sempre no início
    heap_max = []
    for num, freq in quantities.items():
        heap_max.append([-freq, num])

    # Executar o `heapify` no `heap`
    heapq.heapify(heap_max)

    result = []

    for _ in range(k):
        popping = heapq.heappop(heap_max)
        result.append(popping[1])

    return result

print(topKFrequent([1,1,1,2,2,3], k = 2))
print(topKFrequent([-1, -1], k = 1))