
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
# 1000 * 1000 can brute force.
positions = list(map(lambda x : int(x), data.split(",")))

start = min(positions)
end = max(positions)

print("")
print("Part 1")

cost = float('inf')

for i in range(start, end+1):
    fuel = sum(list(map(lambda x : abs(x-i), positions)))
    cost = min(cost, fuel)

print(cost)

print("")
print("Part 2")


# dynamic programming is so fun!
moves = []

# generate all move costs
total = 0
for i in range(max(positions)+1):
    total +=i
    moves.append(total)

cost = float('inf')
for i in range(start, end+1):
    fuel = sum(list(map(lambda x : moves[abs(x-i)], positions)))
    cost = (cost, fuel)

print(cost)

