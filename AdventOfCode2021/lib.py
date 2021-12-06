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

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data

file_sample = ""

lines = read_file(file_Sample).split("\n")