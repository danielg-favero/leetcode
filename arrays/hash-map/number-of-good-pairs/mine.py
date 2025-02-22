def numIdenticalPairs(nums: list[int]) -> int:
    """
    Given an array of integers `nums`, return the number of good pairs.

    A pair `(i, j)` is called good if `nums[i] == nums[j]` and `i < j`.

    Solução: Contar quantas vezes cada número aparece. Se um número aparece `n` vezes,
    é possível fazer `n * (n - 1) // 2` bons pares
    """
    num_count = {}
    good_pairs = 0

    for num in nums:
        if num_count.get(num) is None:
            num_count[num] = 1
        else:
            num_count[num] += 1

    for [_, value] in num_count.items():
        good_pairs += value * (value - 1) // 2

    return good_pairs