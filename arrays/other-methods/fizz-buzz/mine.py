def fizzBuzz(n: int) -> list[str]:
    """
    Given an integer `n`, return a string array `answer` (1-indexed) where:

    - `answer[i] == "FizzBuzz"` if `i` is divisible by `3` and `5`.
    - `answer[i] == "Fizz"` if `i` is divisible by `3`.
    - `answer[i] == "Buzz"` if `i` is divisible by `5`.
    - `answer[i] == i` (as a string) if none of the above conditions are true.
    """
    ans = [str(x + 1) for x in range(n)]

    for i in range(n):
        out = ""
        
        if (i + 1) % 3 == 0: out += "Fizz"
        if (i + 1) % 5 == 0: out += "Buzz"

        ans[i] = out or ans[i]

    return ans

