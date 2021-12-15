
number = "14"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip()

data = read_file(file)

template, rule_lines = data.split("\n\n")
#print(rule_lines)
# data shows that at most a single rule is applied to a pair
rules = dict()
for line in rule_lines.split("\n"):
    #print(line)
    key, value = line.split(" -> ")
    rules[key] = value

print("")
print("Part 1")

elements = dict()

pairs = dict()
# simply trying to count the number of elements, elements are duplicated

# fill with initial elements
for i, e in enumerate(list(template)):
    elements.setdefault(e, 0)
    elements[e] +=1
    if i < len(template) -1:
        pair = e + template[i +1]
        #print(pair)

        pairs.setdefault(pair, 0)
        pairs[pair] += 1


# 10 for the 1st part 40 for the second part

for i in range(40):
    #print(elements)

    new_pairs = dict()
    for pair in pairs.keys():

        # generate all new elements
        if pair in rules:
            v = rules[pair]

            # create a new element
            elements.setdefault(v, 0)
            elements[v] += pairs[pair]

            #print(v)
            # could store in dictionary instead
            pair_left = pair[0] + v
            pair_right = v + pair[1]

            # store the new pairs
            for new_pair in [pair_left, pair_right]:
                new_pairs.setdefault(new_pair, 0)
                new_pairs[new_pair] += pairs[pair]

    # add elements to the set of elements
    pairs = new_pairs


# what are the biggest
values = list(elements.values())
a = max(values)
b = min(values)

#print(a)
#print(b)
print(a - b)



print("")
print("Part 2")

# simply swap from 10 to 40


