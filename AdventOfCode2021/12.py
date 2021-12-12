
number = "12"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip()

data = read_file(file)

# data = '''
# start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end
# '''.strip()

# data = '''
# dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc
# '''.strip()

# data = '''
# fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW
# '''.strip()

# big cave upper case - more than once on a path
# small cave lower case - only once each path
# names can be multiple letters

# breath first search?
# use recursive function?

caves = dict()
for line in data.split("\n"):
    a, b = line.split("-")
    # two way mapping
    if not a in caves:
        caves[a] = set()
    if not b in caves:
        caves[b] = set()

    caves[a].add(b)
    caves[b].add(a)

print("")
print("Part 1")

# return number of paths
def explore(caves, cave, visited):

    # if cave is a small cave an has already been visited return 0
    if cave.islower() and cave in visited:
        return 0

    visited.append(cave)

    # new complete path
    if cave == "end":
        return 1

    # can this infinite loop if two big caves go to each other?
    # yes, but the data has the property that big caves never connect to each other. so safe.

    # Are there dead ends?

    # BFS explore for each possible path
    new_paths = 0
    for connection in caves[cave]:
        new_visit = list(visited) # clone
        new_paths += explore(caves, connection, new_visit)

    return new_paths


v = explore(caves, "start", [])
print(v)



print("")
print("Part 2")

small_caves = list(filter(lambda x: x.islower(), list(set(caves.keys()) - set(["start", "end"]))))

# visited lower = fist lower come across, does that work? yep, because tracking all paths
# need dynamic programming for a path
def explore(caves, paths, cave, visited, visited_same_lower_twice):

    # new complete path
    if cave == "end":
        visited.append(cave)
        paths.append(visited)
        return

    # can only start once
    if cave == "start" and "start" in visited:
        return

    # can visit a SINGLE small cave twice
    # if cave is a small cave and has already been visited twice return 0
    if cave.islower() and cave in visited and not cave == "start":
        if visited_same_lower_twice:
            return
        visited_same_lower_twice = True

    visited.append(cave)


    # can this infinite loop if two big caves go to each other?
    # yes, but the data has the property that big caves never connect to each other. so safe.

    # Are there dead ends?

    # BFS explore for each possible path

    for connection in caves[cave]:
        new_visit = list(visited) # clone
        explore(caves, paths, connection, new_visit, visited_same_lower_twice)

    return

paths = []
explore(caves, paths, "start", [], None)


# paths = list(map(lambda x: ",".join(x), paths))
# paths.sort()
# for p in paths:
#     print(p)

print(len(paths))


