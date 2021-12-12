
number = "11"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip()

data = read_file(file)

def to_ints(s):
    l = list(s)
    return list(map(lambda x: int(x), l))

def get_int_grid(data):
    grid = list(map(
        to_ints, 
        data.split("\n")))
    return grid

def in_bounds(grid, x, y):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

grid_square_left = (-1, 0)
grid_square_right = (1,0)
grid_square_up = (0, -1)
grid_square_down = (0,1)

grid_square_up_right = (1, -1)
grid_square_up_left = (-1, -1)
grid_square_down_right = (1, 1)
grid_square_down_left = (-1, 1)

grid_squares_vertical_horizontal = [grid_square_left, grid_square_right, grid_square_up, grid_square_down]
grid_squares_diagonal = [grid_square_up_right, grid_square_up_left, grid_square_down_right, grid_square_down_left]
grid_squares = [grid_square_left, grid_square_right, grid_square_up, grid_square_down, grid_square_up_right, grid_square_up_left, grid_square_down_right, grid_square_down_left]


print("")
print("Part 1")

grid = get_int_grid(data)

steps = 100
flashes = 0

def octo_flash(grid, x, y):
    grid[y][x] +=1
    v = grid[y][x]
    # flash when it hits 10 but not after
    if v == 10:
        for dx,dy in grid_squares:
            nx = x + dx
            ny = y + dy
            if in_bounds(grid, nx, ny):
                octo_flash(grid, nx, ny)

# flash if greater than 10
# increment fellow squids by one
# an octopus can flash at most once per step

for i in range(steps):

    # increase all energy levels by 1
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            octo_flash(grid, x, y)

    # reset grid and count flashes this round  = all squares > 9
    for y in range(len(grid)):
        for x in range(len(grid)):
            v = grid[y][x]
            if v > 9:
                flashes +=1
                grid[y][x] = 0

 
print(flashes)



print("")
print("Part 2")

# reset grid
grid = get_int_grid(data)

flash = 0
expected_flash = len(grid) * len(grid[0])
steps = 0
while flash < expected_flash:
    flash = 0
    steps +=1
    # increase all energy levels by 1
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            octo_flash(grid, x, y)

    # reset grid and count flashes this round  = all squares > 9
    for y in range(len(grid)):
        for x in range(len(grid)):
            v = grid[y][x]
            if v > 9:
                flash +=1
                grid[y][x] = 0

print(steps)

