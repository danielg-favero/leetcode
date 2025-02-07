def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. 
    You are given an array prerequisites where `prerequisites[i] = [ai, bi]` indicates that you must 
    take course `bi` first if you want to take course `ai`.

    For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
    Return `true` if you can finish all courses. Otherwise, return `false`.
    """

    graph = {i:[] for i in range(numCourses)}

    for a, b in prerequisites:
        graph[b].append(a)

    # 0 = não visitado
    # 1 = visitando
    # 2 = visitado
    state = [0] * numCourses

    def has_cycle(v: int):
        if state[v] == 1:
            return True
        if state[v] == 2:
            return False

        state[v] = 1

        for neighbor in graph[v]:
            if has_cycle(neighbor):
                return True
            
        state[v] = 2
        return False

    for i in range(numCourses):
        if has_cycle(i):
            return False
        
    return True