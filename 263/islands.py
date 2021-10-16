def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    # islands = 0         # var. for the counts
    # .....some operations.....
    # mark_islands(r, c, grid)
    # return islands

    islands = 0

    max_row = len(grid)
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v == 1:
                islands += 1
            mark_islands(r, c, grid)

    return islands


def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    # grid[i][j] = '#'      # one way to mark visited ones - suggestion.

    if grid[i][j] in (0, "#"):
        return

    grid[i][j] = "#"

    # below
    if 0 <= i - 1:
        if 0 <= j < len(grid[i - 1]):
            mark_islands(i - 1, j, grid)

    # beside
    for j_delta in (-1, 1):
        if 0 <= j + j_delta < len(grid[i]):
            mark_islands(i, j + j_delta, grid)

    # above

    if i + 1 < len(grid):
        if 0 <= j < len(grid[i + 1]):
            mark_islands(i + 1, j, grid)
