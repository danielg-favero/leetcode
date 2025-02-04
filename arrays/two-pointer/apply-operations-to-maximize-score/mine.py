def primeScore(n: int) -> int:
    divisor = 2

    # Armazenar uma lista de fatores primos únicos
    unique_prime_factors = set()

    # Percorrer até a raiz quadrada do número
    while divisor * divisor <= n:
        # Adicionar ao conjunto apenas os valores divisíveis pelo divisor
        while n % divisor == 0:
            unique_prime_factors.add(divisor)
            n = n // divisor
        divisor += 1

    if n > 1:
        unique_prime_factors.add(n)
    
    # Retorna a quantidade de únicos fatores primos do conjunto
    return len(unique_prime_factors)

def maximumScore(self, nums: list[int], k: int) -> int:
    """
    You are given an array `nums` of `n` positive integers and an integer `k`.

    Initially, you start with a score of `1`. You have to maximize your score by applying 
    the following operation at most `k` times:

    - Choose any non-empty subarray `nums[l, ..., r]` that you haven't chosen previously.
    - Choose an element `x` of `nums[l, ..., r]` with the highest prime score. 
        If multiple such elements exist, choose the one with the smallest index.
    - Multiply your score by `x`.

    Here, `nums[l, ..., r]` denotes the subarray of `nums` starting at index `l` and ending at the index `r`, 
    both ends being inclusive.

    The prime score of an integer `x` is equal to the number of distinct prime factors of `x`. 
    For example, the prime score of `300` is `3` since `300 = 2 * 2 * 3 * 5 * 5`.

    Return the maximum possible score after applying at most `k operations.

    Since the answer may be large, return it modulo `10^9 + 7`.
    """
    mod = 10**9 + 7
    length = len(nums)
    
    arr = [(index, primeScore(x), x) for index, x in enumerate(nums)]

    left_boundries = [-1] * length
    right_boundries = [length] * length
    stack = []

    # Calcular os limites da esquerda para cada elemento de `arr``
    for index, prime_score in arr:
        while stack and stack[-1][0] < prime_score:
            stack.pop()

        if stack:
            left_boundries[index] = stack[-1][1]
        stack.append((prime_score, index))

    stack.clear()

    # Calcular os limites da direita para cada elemento de `arr``, em ordem contrária
    for index, prime_score in reversed(arr):
        while stack and stack[-1][0] <= prime_score:
            stack.pop()

        if stack:
            right_boundries[index] = stack[-1][1]
        stack.append((prime_score, index))

    # Ordenar `arr` em ordem decrescente com base nos valores de `nums` dentro de `arr`
    arr.sort(key=lambda x: -x[2])

    score = 1
    for index, prime_score, value in arr:
        l, r = left_boundries[index], right_boundries[index]
        count = (index - l) * (r - index)

        if count <= k:
            score = score * pow(value, count, mod) % mod
            k -= count
        else:
            score = score * pow(value, k, mod) % mod
            break

    return score