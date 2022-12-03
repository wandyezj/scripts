
number = "06"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip()

data = read_file(file)
fish = list(map(lambda x : int(x), data.split(",")))

#print("Initial state: {}".format(",".join(list(map(lambda x: str(x), fish)))))

for i in range(80):
    #print("After {:>2} days: {}".format(i, len(fish)))
    # count number to spawn
    spawn = fish.count(0)

    # subtract 1 for each
    fish = list(map(lambda x: x-1, fish))

    # spawn
    for i in range(spawn):
        fish.append(8)

    # map each zero to 6
    fish = list(map(lambda x: 6 if x == -1 else x, fish))

print("")
print("Part 1")

print(len(fish))



print("")
print("Part 2")


# have to use dynamic programming or calculate for value of 256
# have initial generator and then need to extrapolate from there

def spawn_count(fish, window):
    spawns = []

    for i in range(window):
        spawns.append(fish.count(i))
    return spawns


fish = list(map(lambda x : int(x), data.split(",")))
window = 9
days = 256

spawns = spawn_count(fish, window)

for i in range(days):

    # advance
    s0,s1,s2,s3,s4,s5,s6,s7,s8 = spawns
    spawns = [s1,s2,s3,s4,s5,s6, s7+s0, s8, s0]

print(sum(spawns))



