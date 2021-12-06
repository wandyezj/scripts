
number = "05"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data

data = read_file(file).strip()


# create grid
grid = []

size = 1000
for x in range(size):
    row = []
    for y in range(size):
        row.append(0)
    grid.append(row)


for line in data.split("\n"):
    # parse
    a, b = line.split(" -> ")
    ax, ay = a.split(",")
    bx, by = b.split(",")

    ax = int(ax)
    ay = int(ay)
    bx = int(bx)
    by = int(by)

    # plot
    if ax == bx:
        # vertical
        start = ay if ay < by else by
        end = ay if ay > by else by

        x = ax
        for y in range(start, end +1):
            grid[y][x] += 1

    elif ay == by:
        # horizontal
        start = ax if ax < bx else bx
        end = ax if ax > bx else bx
        
        y = ay
        for x in range(start, end +1):
            grid[y][x] += 1
    else:
        # Part 2 addition - comment out for part 1
        # diagonal
        # these are perfect 45 degree diagonals
        # meaning dx and dy are equal
        length = abs(ax - bx)

        # directions
        dx = 1 if ax < bx else -1
        dy = 1 if ay < by else -1

        # trace from a to b
        x = ax
        y = ay
        for i in range(length+1):
            # mark
            grid[y][x] += 1
            # update
            x += dx
            y += dy


# count
overlap = 0
for y in range(len(grid)):
    for x in range(len(grid[x])):

        o = grid[y][x]
        #print(o if o > 0 else ".", end="")
        if o >=2:
            overlap +=1
    #print()


print(overlap)

