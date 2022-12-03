
number = "13"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip()

data = read_file(file)

dot_lines, fold_lines = data.split("\n\n")

def parse_dot(line):
    xs, ys = line.split(",")
    x = int(xs)
    y = int(ys)
    return x,y

dots = list(map(parse_dot, dot_lines.strip().split()))

def parse_fold(line):
    _, _, s = line.split(" ")
    axis, value = s.split("=")
    return (axis, int(value))

folds = list(map(parse_fold, fold_lines.strip().split("\n")))

print("")
print("Part 1")

'''
change coordinates depending on the dots

fold along x means change the x coordinate, fold along y means change the y coordinate
looking to have sets of coordinates

equation for dot transposition

if < fold line no transposition



can the fold make coordinates negative if so must readjust dots

always folds in half

'''



def fold_value(c, value):

    if c == value:
        return None

    elif c > value:
        return (value * 2) - c

    return c

def new_fold_dots(dots, fold):
    axis, value = fold
    new_dots = set()
    for x, y in dots:

        new_x = x
        new_y = y
        if axis == "x":
            new_x = fold_value(x, value)

        elif axis == "y":
            new_y = fold_value(y, value)

        if new_x != None and new_y != None:
            new_dot = (new_x, new_y)
            new_dots.add(new_dot)

    return new_dots

fold = folds[0]
print(fold)

dots = set(dots)
new_dots = new_fold_dots(dots, fold)
print(len(new_dots))




print("")
print("Part 2")

new_dots =dots
for fold in folds:
    new_dots = new_fold_dots(new_dots, fold)
    #print(len(new_dots))

# plot dots
# could also look at min values of the folds since it can't be greater than that
max_x = max(list(map(lambda v: v[0], new_dots)))
max_y = max(list(map(lambda v: v[1], new_dots)))
# print(max_x)
# print(max_y)

for y in range(max_y + 1):
    line = ""
    for x in range(max_x + 1):
        dot = (x, y)
        c = "."
        if dot in new_dots:
            c = "#"

        line += c


    print(line)



