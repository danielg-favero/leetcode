def countBits(n: int) -> list[int]:
    """
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
    ans[i] is the number of 1's in the binary representation of i.
    """
    ans = []

    for i in range(n + 1):
        k = i
        sum_of_1 = 0
        while k:
            sum_of_1 += k & 1
            k = k >> 1
        
        ans.append(sum_of_1)
    return ans

print(countBits(5))