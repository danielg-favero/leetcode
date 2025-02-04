def choose(n, k):
    res = 1

    if k > n - k:
        k = n - k

    for i in range(k):
        res *= (n - i)
        res //= (i + 1)

    return res

def generate(self, numRows: int) -> list[list[int]]:
    """
    Given an integer `numRows`, return the first numRows of Pascal's triangle.
    """

    result = []

    # Percorrer todas as linhas
    for row in range(1, numRows + 1):
        row_coeffs = []
        # Cada `n-ésima` linha tem exatamente `n` elementos
        for i in range(row):
            # Os elementos da pirâmide de pascal são obtidos pelo binômio de Newton
            row_coeffs.append(choose(row, i))
        result.append(row_coeffs)

    return result