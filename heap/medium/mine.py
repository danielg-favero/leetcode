import heapq

def topKFrequent(nums: list[int], k: int) -> list[int]:
    """
    Given an integer array `nums` and an integer `k`, 
    return the `k` most frequent elements. 

    You may return the answer in any order.
    """

    hash_map = {}

    # Contar quantas vezes cada elementos repete no array
    for num in nums:
        if hash_map.get(num) is None:
            hash_map[num] = 1
        else:
            hash_map[num] += 1

    # Criar uma heap
    heap = []

    # Armazenar os elementos em uma heap, adicionando ele de forma negativa, assim o "Menor" valor estará sempre no início
    for num, count in hash_map.items():
        heapq.heappush(heap, (-count, num))
    
    result = []
    for _ in range(k):
        _, num = heapq.heappop(heap)
        result.append(num)

    return result

print(topKFrequent([1,1,1,2,2,3], k = 2))
print(topKFrequent([-1, -1], k = 1))