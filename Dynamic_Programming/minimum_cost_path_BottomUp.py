"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
INFINITY = float('inf')  # Same as math.inf

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid

def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    #table = [[None] * n_cols for i in range(len(grid))]
    for i in range(1, n_rows):
        for j in range(n_cols):
            if j == 0:
                grid[i][j] += min(grid[i - 1][0:2])
            elif j == n_cols - 1:
                grid[i][j] += min(grid[i - 1][j-1:])
            else:
                grid[i][j] += min(grid[i - 1][j-1:j+2])
            
    best = min(grid[-1])
    return best
    
    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

# --------------test1-----------------------------
print(file_cost('checkboard.txt'))
# ------------------------------------------------
