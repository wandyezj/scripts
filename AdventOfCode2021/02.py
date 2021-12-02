number = "02"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip()

def read_file_lines(file):
    data = read_file(file)
    lines = data.split("\n")
    return lines

def read_file_lines_int(file):
    ints = []
    for line in lines:
        n = int(number)
        ints.append(n)
    return ints

def read_file_lines_list(file):
    lines = read_file_lines(file)
    lists = []
    for line in lines:
        l = line.strip().split()
        lists.append(l)
    return lists



print("Part 1")

lines = read_file_lines(file)


depth = 0
position = 0


for line in lines:
    c, n = line.strip().split()
    n = int(n)
    #print(c)
    #print(n)

    if c == "forward":
        position += n

    if c == "up":
        depth -= n

    if c== "down":
        depth += n

print(depth * position)

aim = 0
position = 0
depth = 0

for line in lines:
    c, n = line.strip().split()
    n = int(n)

    if c == "forward":
        position += n
        depth += aim * n

    if c == "up":
        aim -= n

    if c== "down":
        aim += n

print(depth * position)

