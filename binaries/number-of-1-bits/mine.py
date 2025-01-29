def hammingWeight(n: int) -> int:
    """
    Given a positive integer n, write a function that returns the number of set bits
    in its binary representation (also known as the Hamming weight).
    """

    weight = 0
    while n:
        weight += n & 1
        n = n >> 1
    
    return weight

print(hammingWeight(128))