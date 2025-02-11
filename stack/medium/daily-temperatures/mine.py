def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """
    Given an array of integers `temperatures` represents the daily temperatures, 
    return an array `answer` such that `answer[i]` is the number of days you have 
    to wait after the `ith` day to get a warmer temperature. If there is no future 
    day for which this is possible, keep `answer[i] == 0` instead.
    """

    ans = [0] * len(temperatures)
    stack = []

    for idx, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            index = stack.pop()
            ans[index] = idx - index
        stack.append(idx)

    return ans

print(dailyTemperatures([73,74,75,71,69,72,76,73]))