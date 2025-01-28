def bubble_sort(nums: list[int]):
    """
    Complexidade temporal:
    - Melhor caso: `O(n)`
    - Pior caso: `O(nˆ2)`

    Complexidade espacial: `O(1)` (Não precisa alocar nenhum estrutra de dados adicional)
    """
    size = len(nums)
    for _ in nums:
        for i in range(size - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        size -= 1

nums = [5, 1, 7,4, 3, 2, 6]
bubble_sort(nums)

print(nums)