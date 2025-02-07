import heapq

def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    """
    You are given a network of `n` nodes, labeled from `1` to `n`. 
    You are also given `times`, a list of travel times as directed edges 
    `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, 
    and `wi` is the time it takes for a signal to travel from source to target.

    We will send a signal from a given node `k`. Return the minimum time it takes for 
    all the n nodes to receive the signal. If it is impossible for all the `n` nodes 
    to receive the signal, return `-1`.

    Solução: Dijkstra, por que queremos encontrar o menor caminho
    """

    graph = {}

    for t in times:
        if not graph.get(t[0]):
            graph[t[0]] = { t[1]: t[2] }
        else:
            graph[t[0]][t[1]] = t[2]

    distances = { k: 0 }
    min_heap = [(0, k)]


    while min_heap:
        current_distace, current_node = heapq.heappop(min_heap)

        connections = graph.get(current_node)

        if connections:
            for key, v in connections.items():
                graph_distance = distances.get(key, float('inf'))

                if current_distace + v < graph_distance:
                    distances[key] = current_distace + v
                    heapq.heappush(min_heap, (current_distace + v, key))

    _max = -1
    if len(distances) < n:
        return _max
    
    for key, v in distances.items():
        _max = max(_max, v)

    if _max == 0: return -1
    return _max