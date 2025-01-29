def missingNumber(nums: list[int]) -> int:
    """
    Given an array nums containing `n` distinct numbers in the range [0, n], 
    return the only number in the range that is missing from the array.

    Possível solução: XOR
    """

    x = 0
    for num in nums:
        x = x ^ num

    for i in range(len(nums) + 1):
        x = x ^ i

    return x

missingNumber([3, 0, 1])