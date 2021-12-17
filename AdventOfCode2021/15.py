
number = "15"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip()

def write_file(file, data):
    f = open(file, 'w')
    f.write(data)
    f.close()

data = read_file(file)

def to_ints(line):
    l = list(line)
    return list(map(lambda x: int(x), l))

# grid[y][x] of numbers 0-9
def get_int_grid(data):
    grid = list(map(
        to_ints, 
        data.split("\n")))
    return grid

# data = """19
# 19"""

grid = get_int_grid(data)
#print(grid)




# grid[y][x]
# grid whe max y = my and max x = mx
def make_grid(mx, my, value=0):
    grid = []
    for x in range(mx):
        row = []
        for y in range(my):
            row.append(value)
        grid.append(row)
    return grid

# make empty grid same size as the passed in grid
def make_empty_grid(grid, value = 0):
    return make_grid(len(grid[0]), len(grid), value)

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

def in_bounds(grid, x, y):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

# points generated from offsets of x and y that are within grid bounds
def in_bound_offset_points(grid, x,y, offsets):
    points = list(map(lambda p : (x + p[0], y + p[1]), offsets))
    ok = list(filter(lambda p: in_bounds(grid, p[0], p[1]), points))
    return ok

def string_grid(grid, template = "{:>1}"):
    s = ""
    for y in grid:
        s += "".join(list(map(lambda s: template.format(s), y))) + "\n"

    return s

def print_grid(grid, template = "{:>1}"):
    s = string_grid(grid, template)
    print(s)

#print_grid(grid)


def increment_grid(grid, n):
    # generate a new grid modified by (v + n) % 9 + 1
    new_grid = []
    for y in grid:
        row = []
        for x in y:
            v = (x - 1 + n) % 9 + 1
            row.append(v)

        new_grid.append(row)

    return new_grid

# scale grid up 5 X
def scale_grid(grid):
    size = 5
    new_grid = increment_grid(grid, 0)

    # expand across
    for ix in range(1,size):
        g = increment_grid(grid, ix)

        for i in range(len(new_grid)):
            new_grid[i].extend(g[i])

    new_grid_row = increment_grid(new_grid, 0)
    # expand down
    for iy in range(1, size):
        g = increment_grid(new_grid_row, iy)

        for row in g:
            new_grid.append(row)

    return new_grid

# print_grid(grid)
# print()
# print_grid(increment_grid(grid, 1))

# print_grid(scale_grid(grid))
# print_grid(grid)

# comment out for part 2
grid = scale_grid(grid)


# write_file("grid_scale.txt", string_grid(grid))
# print_grid(grid)


# is this just Dijkstras algorithm? https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
# every x, y is a node and edge cost is value at the node


print("")
print("Part 1")





start = (0,0)
end = (len(grid) -1, len(grid) -1)

# 1. 
# will generate unvisited as we go
unvisited = set([start])
visited = set()

# 2. assign every node a tentative distance
distance = make_empty_grid(grid, len(grid) * 2 * 10) # set distance to practical infinity
# set distance to zero for the initial node
distance[0][0] = 0
grid[0][0] = 0




# 5. if destination visited done!
while len(unvisited) > 0 and not end in visited:

    # pick node with the smallest distance
    to_visit = list(unvisited)
    distances = list(map(lambda p : distance[p[1]][p[0]], to_visit))
    m = min(distances)
    index = distances.index(m)

    # start
    current = to_visit[index]
    #print(current)
    #print_grid(distance)

    # 3. consider all unvisited neighbors
    current_x, current_y = current
    current_value = distance[current_y][current_x]

    grid_neighbor_offsets = grid_squares_vertical_horizontal #[grid_square_down, grid_square_right]

    neighbors = in_bound_offset_points(grid, current_x, current_y, grid_neighbor_offsets)
    for nx, ny in neighbors:
        n = (nx, ny)
        if n in visited:
            continue

        alt = grid[ny][nx] + current_value

        if alt < distance[ny][nx]:
            distance[ny][nx] = alt

        unvisited.add(n)

    # 4. mark the current node as visited
    visited.add(current)
    unvisited.remove(current)


end_x, end_y = end
print(distance[end_y][end_x])


print("")
print("Part 2")

