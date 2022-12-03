
number = "09"
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

grid = list(map(
    to_ints, 
    data.split("\n")))


print("")
print("Part 1")

lows = []

for y in range(len(grid)):
    print()
    for x in range(len(grid[y])):
        center_value = grid[y][x]
        #print("({},{}) = {} ".format(x,y, center_value))
        # x y
        all_work = True
        checks = [(0,1), (0, -1), (1,0),(-1, 0)]
        for dx, dy in checks:
            #print("    {} {} ".format(dx,dy))
            cx = x + dx
            cy = y + dy

            in_bound_x = cx >= 0 and cx < len(grid[y])
            in_bound_y = cy >= 0 and cy < len(grid)

            if in_bound_x and in_bound_y:
                value = grid[cy][cx]
                compare = center_value < value
                #print("        {} < {} -> {}".format(value, center_value, compare))

                if not compare:
                    all_work = False
                    #print("        BAD")

        if all_work:
            #print("APPEND")
            lows.append(center_value)
            #print(center_value)
        #print()

#print(lows)
print(sum(lows) + len(lows))


print("")
print("Part 2")

# basin search
# store size of three biggest basins, so store size of all basins sort and pop the last 3
# every value is part of at a basin, if already counted ignroe it.
# mark values already counted with None
# 9 does not count as being part of a basin

# really a better way would be to have a grid that counts how many neighbors are > it and set that value, then simply sum across values

def in_bounds(x,y, grid):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

def basin_size(x,y, grid, v_parent, visited):

    if not in_bounds(x,y,grid):
        return 0



    v = grid[y][x]

    if v == 9:
        # basin size is zero
        return 0

    # compare v with v parent
    # check that values are bigger
    if v > v_parent:
        # counted
        #grid[y][x] = 9

        key = (x,y)
        if (key in visited):
            return 0
        visited.add(key)

        checks = [(0,1), (0, -1), (1,0),(-1, 0)]
        return sum(list(map(lambda d : basin_size(x + d[0], y + d[1], grid, v, visited) , checks))) + 1

    return 0

    




sizes = []

for y in range(len(grid)):
    for x in range(len(grid[y])):
        size = basin_size(x,y, grid, -1, set())
        if size > 0:
            sizes.append(size)

sizes.sort()
print(sizes)
found = sizes[-3:]
print(found)
import math
print(math.prod(found))


#print(grid)