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
    max_in_rows = []
    max_in_columns = []

    for r in range(len(grid)):
        max_in_rows.append(max(grid[r]))

    for r in range(len(grid)):
        x = 0
        for c in range(len(grid)):
            x = max(x, grid[c][r])
        max_in_columns.append(x)
            
    for r in range(len(grid)):
        for c in range(len(grid)):
            increase += min(max_in_rows[r], max_in_columns[c]) - grid[r][c]

    return increase

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(maxIncreaseKeepingSkyline(grid))