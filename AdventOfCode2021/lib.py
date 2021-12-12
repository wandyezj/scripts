# flip string of zeros and ones example: 1010 <-> 0101
def flip_bits(n):
    return "".join(list(map(lambda x: "1" if x == "0" else "0", list(n))))



# grid[y][x]
# grid whe max y = my and max x = mx
def make_grid(mx, my):
    grid = []
    for x in range(mx):
        row = []
        for y in range(my):
            row.append(0)
        grid.append(row)
    return grid

# grid[y][x]
# mx and my are the maximum x and y value that can be passed to the grid `<=`
def expand_grid(grid, mx, my):
    while len(grid) <= my:
        grid.append([])

    for y in range(len(grid)):
        while len(grid[y]) <= mx:
            grid[y].append(0)

def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[x])):
            o = grid[y][x]
            print(o, end="")
    print()

def in_bounds(grid, x, y):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

# Grid square neighbor offsets

grid_square_left = (-1, 0)
grid_square_right = (1,0)
grid_square_up = (0, -1)
grid_square_down = (0,1)

grid_square_up_right = (1, -1)
grid_square_up_left = (-1, -1)
grid_square_down_right = (1, 1)
grid_square_down_left = (-1, 1)

grid_squares_vertical = [grid_square_up, grid_square_down]
grid_squares_horizontal = [grid_square_left, grid_square_right]
grid_squares_vertical_horizontal = grid_squares_vertical + grid_squares_horizontal
grid_squares_diagonal = [grid_square_up_right, grid_square_up_left, grid_square_down_right, grid_square_down_left]
grid_squares = grid_squares_vertical_horizontal  + grid_squares_diagonal

def to_ints(line):
    l = list(line)
    return list(map(lambda x: int(x), l))

# grid[y][x] of numbers 0-9
def get_int_grid(data):
    grid = list(map(
        to_ints, 
        data.split("\n")))
    return grid

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data

file_sample = ""

lines = read_file(file_Sample).split("\n")