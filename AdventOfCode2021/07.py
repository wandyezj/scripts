
number = "07"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip()

data = read_file(file)

# data has about 1000 numbers
positions = list(map(lambda x : int(x), data.split(",")))


def fuel(positions, i):
    return sum(list(map(lambda x : abs(x-i), positions)))

# dynamic programming is so fun!
moves = []

# generate all moves
total = 0
for i in range(max(positions)+1):
    total +=i
    moves.append(total)

def get_move_cost(d):
    return moves[d]

def fuel2(positions, i):
    return sum(list(map(lambda x : get_move_cost(abs(x-i)), positions)))

print("")
print("Part 1")

# 1000 * 1000 can brute force?

start = min(positions)
end = max(positions)

costs = []

for i in range(start, end+1):
    costs.append(fuel(positions, i))

print(min(costs))


print("")
print("Part 2")

# more dynamic programming
costs = []
for i in range(start, end+1):
    costs.append(fuel2(positions, i))
#print(moves)
print(min(costs))

