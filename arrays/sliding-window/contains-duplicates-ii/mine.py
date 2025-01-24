def containsNearbyDuplicateMine(nums: list[int], k: int) -> bool:
    """
    Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
    """

    already_found = {}

    for i in range(len(nums)):
        if nums[i] not in already_found:
            already_found[i] = nums[i]
            continue

        for j in range(i + 1, len(nums)):
            if abs(i - j) > k: continue
            if nums[i] == nums[j]:
                return True

    return False