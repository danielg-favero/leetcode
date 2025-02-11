def summaryRanges(nums: list[int]) -> list[str]:
    """
    You are given a sorted unique integer array `nums`.

    A range `[a,b]` is the set of all integers from `a` to `b` (inclusive).

    Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
    That is, each element of `nums` is covered by exactly one of the ranges, 
    and there is no integer `x` such that `x` is in one of the ranges but not in nums.

    Each range `[a,b]` in the list should be output as:

    `"a->b"` if `a != b`
    `"a"` if `a == b`
    """
    l, r = 0, 0
    result = []

    while r < len(nums):
        a = nums[l]

        while r < len(nums) - 1 and nums[r] == nums[r + 1] - 1:
            r += 1

        b = nums[r]

        if a != b:
            result.append(f"{a}->{b}")
        else:
            result.append(f"{a}")
        l = r + 1
        r = l

    return result

print(summaryRanges([0,2,3,4,6,8,9]))
print(summaryRanges([0, 1, 2, 4, 5, 7]))
