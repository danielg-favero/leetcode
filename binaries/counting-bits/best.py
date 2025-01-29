def countBits(n: int) -> list[int]:
    """
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
    ans[i] is the number of 1's in the binary representation of i.
    """
    res = []
    while n > -1:
        temp = n
        count = 0
        while temp:
            count += temp & 1
            temp = temp >> 1
        res.append(count)
        n-=1
    return res[::-1]

print(countBits(5))