def searchInsert(nums: list[int], target: int) -> int:
    """
    Given a sorted array of distinct integers and a target value, 
    return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with `O(log n)` runtime complexity.

    Possível solução: Busca Binária
    """

    l = 0
    r = len(nums)

    while l < r:
        mid = int((l + r) / 2)

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid

    if l == 0:
        return 0
    if r == len(nums) - 1:
        return r
    else:
        return l


print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3], 2))
