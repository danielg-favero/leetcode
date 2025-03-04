import math

def getAverages(nums: list[int], k: int) -> list[int]:
    """
    You are given a 0-indexed array `nums` of `n` integers, and an integer `k`.

    The k-radius average for a subarray of `nums` centered at some index `i` 
    with the radius `k` is the average of all elements in nums between the 
    indices `i - k` and `i + k` (inclusive). If there are less than `k` elements 
    before or after the index `i`, then the k-radius average is `-1`.

    Build and return an array avgs of length `n` where `avgs[i]` is the 
    k-radius average for the subarray centered at index `i`.

    The average of `x` elements is the sum of the `x` elements divided by `x`, using integer division. 
    The integer division truncates toward zero, which means losing its fractional part.

    - For example, the average of four elements `2`, `3`, `1`, and `5` is `(2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75`, 
    which truncates to `2`.

    Solução: Sliding Window
    """
    n = len(nums)
    avgs = [-1] * n
    window_sum = 0

    for idx, num in enumerate(nums):
        window_sum += num

        if idx >= 2 * k:
            left_radius = idx - k
            right_radius = idx + k
            count = right_radius - left_radius + 1
            avgs[idx - k] = math.trunc(window_sum / count)
            window_sum -= nums[idx - 2 * k]

    return avgs