number = "03"
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
    lines = read_file_lines(file)
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


lines = read_file_lines(file)

total = len(lines[0])

print("Part 1")
created = ""

for i in range(total):
    ones = 0
    zeros = 0
    for line in lines:
        #print(line)
        bit = line[i]
        if bit == '1':
            ones +=1

        if bit =='0':
            zeros +=1


    if ones > zeros:
        created = created + "1"
    else:
        created = created + "0"

gamma = created
#print(gamma)

def invert(bits):
    created = ""
    for c in bits:
        if c == "1":
            created += "0"
        else:
            created += "1"
    return created

epsilon = invert(gamma)
#print(epsilon)

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)


print("Part 2")

def count_bit(numbers, i):
    ones = 0
    zeros = 0
    for n in numbers:

        bit = n[i]
        if bit == '1':
            ones +=1

        if bit =='0':
            zeros +=1
    return (zeros, ones)



def filter_down(original, prefix):
    next = []
    for v in original:
        if v.startswith(prefix):
            next.append(v)
    if len(next) == 0:
        next.append(original[-1])
    return next


def oxygen_generator_rating(lines):
    set_most_common = lines
    created_most_common = ""

    for i in range(total):
        zeros, ones = count_bit(set_most_common, i)
        #print(ones, zeros)

        if ones == zeros:
            created_most_common += "1"
        elif ones > zeros:
            created_most_common += "1"
        else:
            created_most_common += "0"

        set_most_common = filter_down(set_most_common, created_most_common)
        #print(set_most_common)
        if len(set_most_common) == 1:
            return set_most_common[0]

def co_scrubber_rating(lines):
    set_most_common = lines
    created_most_common = ""

    for i in range(total):
        zeros, ones = count_bit(set_most_common, i)
        #print(ones, zeros)

        if ones == zeros:
            created_most_common += "0"
        elif ones > zeros:
            created_most_common += "0"
        else:
            created_most_common += "1"

        set_most_common = filter_down(set_most_common, created_most_common)
        #print(set_most_common)
        if len(set_most_common) == 1:
            return set_most_common[0]


o2 = oxygen_generator_rating(lines)
#print(o2)
co = co_scrubber_rating(lines)
#print(co)

a = int(o2, 2)
b = int(co, 2)
print(a * b)
