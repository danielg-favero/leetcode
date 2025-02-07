def maximumBags(capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        """
        You have `n` bags numbered from `0` to `n - 1`. You are given two `0-indexed` 
        integer arrays capacity and rocks. The ith bag can hold a maximum of `capacity[i]` 
        rocks and currently contains `rocks[i]` rocks. You are also given an integer additionalRocks, 
        the number of additional rocks you can place in any of the bags.

        Return the maximum number of bags that could have full capacity after placing the additional 
        rocks in some bags.

        Solução: Método Guloso
        """

        full_bags = 0
        
        for idx in range(len(rocks)):
            rocks[idx] = capacity[idx] - rocks[idx]

        rocks.sort()

        i = 0
        while i < len(rocks) and rocks[i] <= additionalRocks:
            full_bags += 1
            additionalRocks -= rocks[i]
            i += 1

        return full_bags