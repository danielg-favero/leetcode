def numIslands(grid: list[list[str]]) -> int:
    """
    Given an `m x n` 2D binary grid `grid` which represents a map of 
    `'1's` (land) and `'0's` (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent 
    lands horizontally or vertically. You may assume all four edges of 
    the grid are all surrounded by water.

    Solução: DFS
    """

    if not grid: return 0

    islands = 0
    rows, columns = len(grid), len(grid[0])
    visited_land = set()

    # Realizar uma dfs para preencher o conjunto de caminhos percorridos
    def dfs(row: int, column: int):
        # Não realizar o dfs se está em água ou em uma terra visitada
        if (row, column) in visited_land or row < 0 or column < 0 or row >= rows or column >= columns or grid[row][column] == '0': return

        # Adicionar ao conjunto de visitados
        visited_land.add((row, column))

        # Percorrer os nós adjacentes
        dfs(row + 1, column)
        dfs(row - 1, column)
        dfs(row, column + 1)
        dfs(row, column - 1)

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == '1' and (row, column) not in visited_land:
                dfs(row, column)
                islands += 1

    return islands

