def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    """
    Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
    """

    d = {}

    for idx, x in enumerate(nums):
        if x in d and abs(idx - d[x] ) <= k:
            return True
        else:
            d[x] = idx

    return False