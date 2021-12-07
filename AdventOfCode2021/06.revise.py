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


def population(fish, days):

    spawns = []

    for i in range(9):
        spawns.append(fish.count(i))

    for i in range(days):

        spawn = spawns.pop(0)
        spawns.append(spawn)
        spawns[6] += spawn

    return sum(spawns)


print("")
print("Part 1")
print(population(fish, 80))

print("")
print("Part 2")
print(population(fish, 256))

