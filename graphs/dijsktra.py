import heapq

def dijkstra(graph, start):
    min_heap = [(0, start)] # Fila de processamento, inicialmente inicia com [(0, 'A')]
    distances = { node: float('inf') for node in graph }
    distances[start] = 0

    while min_heap:
        # Aqui o heap funciona como uma fila de prioridades
        # Processando os elementos de menor valor antes
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]: continue

        # Acessar todos os vizinhos
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1 },
}