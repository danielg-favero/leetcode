def gameOfLife(board: list[list[int]]) -> None:
    """
    According to Wikipedia's article: "The Game of Life, also known simply as Life, 
    is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

    The board is made up of an `m x n` grid of cells, where each cell has an initial 
    state: live (represented by a `1`) or dead (represented by a `0`). 
    Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
    using the following four rules (taken from the above Wikipedia article):

    1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by over-population.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    The next state of the board is determined by applying the above rules simultaneously 
    to every cell in the current state of the `m x n` grid `board`. In this process, births and 
    deaths occur simultaneously.

    Given the current state of the `board`, update the `board` to reflect its next state.

    Note that you do not need to return anything.

    Solução:
    - Percorrer o `board` uma primeira vez:
        - Marcar a próxima geração morta como 2
        - Marcar a próxima geração viva como -1
    - Percorrer o `board` uma segunda vez:
        - Substituir os valores
    """

    rows, columns = len(board), len(board[0])

    for row in range(rows):
        for column in range(columns):
            live_neighbors = -board[row][column]

            for x in range(row - 1, row + 2):
                for y in range(column - 1, column + 2):
                    if 0 <= x <= rows - 1 and 0 <= y <= columns - 1 and board[x][y] > 0:
                        live_neighbors += 1
            
            if board[row][column] and (live_neighbors < 2 or live_neighbors > 3): 
                board[row][column] = 2
            elif board[row][column] == 0 and live_neighbors == 3: 
                board[row][column] = -1

    for row in range(rows):
        for column in range(columns):
            if board[row][column] == 2:
                board[row][column] = 0
            elif board[row][column] == -1:
                board[row][column] = 1

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
gameOfLife(board)
print(board)