def findJudge(n: int, trust: list[list[int]]) -> int:
    """
    In a town, there are `n` people labeled from `1` to `n`.
    There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:
    1. The town judge trusts nobody.
    2. Everybody (except for the town judge) trusts the town judge.
    3. There is exactly one person that satisfies properties `1` and `2`.

    You are given an array `trust` where `trust[i] = [ai, bi]` representing that the person labeled `ai` trusts the person labeled `bi`. 
    If a trust relationship does not exist in `trust` array, then such a trust relationship does not exist.

    Return the label of the town judge if the town judge exists and can be identified, or return `-1` otherwise.
    """

    if len(trust) == 0 and n == 1: return 1

    trust_count = [0] * (n + 1)

    for person in trust:
        trust_count[person[0]] -= 1
        trust_count[person[1]] += 1

    for person in range(len(trust_count)):
        if trust_count[person] == n - 1: return person

    return -1

findJudge(3, [[1,3],[2,3]])
findJudge(3, [[1,3],[2,3],[3,1]])