def partition(nums: list[int], left: int, right: int):
    pivot = nums[right]

    i = left - 1

    for j in range(left, right):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[right] = nums[right], nums[i + 1]

    return i + 1

def quick_sort(nums: list[int], left: int, right: int):
    """
    Complexidade temporal:
    - Melhor caso: `O(nlogn)`
    - Caso médio: `O(nlogn)`
    - Pior caso: `O(nˆ2)`

    Complexidade espacial: 
    - Melhor caso: `O(logn)`
    - Caso médio: `O(logn)`
    - Pior caso: `O(n)`
    """

    # Se o left for igual o right, todos os subarrays foram ordenados
    if left < right:
        pivot = partition(nums, left, right)
        quick_sort(nums, left, pivot - 1)
        quick_sort(nums, pivot + 1, right)

nums = [5, 1, 7,4, 3, 2, 6]
quick_sort(nums, 0, len(nums) - 1)

print(nums)