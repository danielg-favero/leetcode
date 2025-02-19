def climbStairs(n: int) -> int:
    """
    You are climbing a staircase. It takes `n` steps to reach the top.

    Each time you can either climb `1` or `2` steps. 
    In how many distinct ways can you climb to the top?

    Solução: Programação Dinâmica, igual ao algoritmo de fibonacci
    """
    if n == 0: return 0
    if n == 1: return 1

    steps = [1, 2]

    for i in range(2, n):
        steps.append(steps[i - 1] + steps[i - 2])

    return steps[-1]

print(climbStairs(4))