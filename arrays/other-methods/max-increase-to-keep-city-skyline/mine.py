def maxIncreaseKeepingSkyline(grid: list[list[int]]) -> int:
    """
    There is a city composed of `n x n` blocks, where each block contains a single building
    shaped like a vertical square prism. You are given a `0`-indexed `n x n` integer matrix `grid` 
    where `grid[r][c]` represents the height of the building located in the block at row r and column c.

    A city's skyline is the outer contour formed by all the building when viewing the side of the city
    from a distance. The skyline from each cardinal direction north, east, south, and west may be different.

    We are allowed to increase the height of any number of buildings by any amount 
    (the amount can be different per building). The height of a `0`-height building can also be increased.
    However, increasing the height of a building should not affect the city's skyline 
    from any cardinal direction.

    Return the maximum total sum that the height of the buildings can be increased by 
    without changing the city's skyline from any cardinal direction.
    """

    increase = 0
    transposed_grid = []

    # NOTA: Não é necessário transpor toda a matriz, apenas pegar os valores maíores de cada coluna
    for r in range(len(grid)):
        column = []
        for c in range(len(grid[r])):
            column.append(grid[c][r])
        transposed_grid.append(column)
    
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            max_in_row = max(grid[r])
            max_in_column = max(transposed_grid[c])
            
            min_building_height = min(max_in_row, max_in_column)
            height_diff = min_building_height - grid[r][c]
            increase += height_diff
            grid[r][c] += height_diff # Não é necessário armazenar o valor modificado

    return increase

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(maxIncreaseKeepingSkyline(grid))