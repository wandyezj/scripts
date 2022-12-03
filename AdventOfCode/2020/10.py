def readFile(file):
    f = open(file)
    data = f.read()
    f.close()
    return data

def readFileLines(file):
    data = readFile(file)
    return data.strip().split("\n")

def readFileNumberList(file):
    lines = readFileLines(file)
    return list(map(int, lines))

def differencesBetweenNumbers(numbers):
    # only allowed to have four levels of difference 
    differences = dict()

    previous = 0
    for current in numbers:
        delta = current - previous

        if not delta in differences:
            differences[delta] = 0
        differences[delta] += 1

        previous = current

    return differences

numbers = readFileNumberList("10.input.txt")

# add start and end
real_begin = 0
real_end = max(numbers) + 3
numbers.append(real_begin) # starts a 0 anyway
numbers.append(real_end)
numbers.sort()

print(numbers)

print("Part 1")

deltas = differencesBetweenNumbers(numbers)
ones = deltas[1]
threes = deltas[3]
print(ones * threes)


print("Part 2")
#print(ones)
#print(threes)

def generateComboOne(numbers):
    combos = []
    for i in range(len(numbers)):
        v = [numbers[i]]
        combos.append(v)
    return combos

def generateComboTwo(numbers):
    combos = []
    sequence = []
    for a in range(len(numbers)):
        sequence.append(numbers[a])
        for b in range(a +1,len(numbers)):
            sequence.append(numbers[b])
            combos.append(sequence)
            sequence = []
    return combos

def generateComboThree(numbers):
    combos = []
    sequence = []
    for a in range(len(numbers)):
        sequence.append(numbers[a])
        for b in range(a +1,len(numbers)):
            sequence.append(numbers[b])
            for c in range(b +1,len(numbers)):
                sequence.append(numbers[c])
                combos.append(sequence)
                sequence = []
    return combos

# def generateComboFour(numbers):
#     combos = []
#     sequence = []
#     for a in range(len(numbers)):
#         sequence.append(numbers[a])
#         for b in range(a + 1,len(numbers)):
#             sequence.append(numbers[b])
#             for c in range(b + 1,len(numbers)):
#                 sequence.append([numbers[c]])
#                 for d in range(c + 1,len(numbers)):
#                 sequence.append([numbers[d]])
#                 combos.append(sequence)
#                 sequence = []
#     return combos

def validCombo(begin, end, combo):
    # can it hook up to begin?
    #print("\t{}".format(combo))
    if combo[0] -3 > begin:
        return False
    
    # can it hook up to end?
    if combo[-1] +3 < end:
        return False

    # check that each number only differs bu at most 3
    for i in range(len(combo) -1):
        if combo[i] +3 < combo[i+1]:
            return False

    return True

def validComboCount(begin, end, combos):

    count = 0
    for c in combos:
        if validCombo(begin, end, c):
            count += 1
    return count

def combinationsBetween(begin, between, end):
    count = 1 # all always works
    # does none work?
    if begin +3 >= end:
        count += 1

    if len(between) ==0:
        return 0
    
    if len(between) == 1:
        # with or without the number
        return count
    
    if len(between) == 2:
        a = between[0]
        b = between[1]

        # a can work by itself
        if a + 3 >= end:
            count +=1
        
        # b can work by itself
        if b - 3 <= begin:
            count +=1
        return count

    if len(between) == 3:
        # generate all sequences and count each one that works
        combos = generateComboOne(between)
        combos.extend(generateComboTwo(between))
        #print(combos)
        count += validComboCount(begin, end, combos)
        
        return count

    if len(between) == 4:
        combos = generateComboOne(between)
        combos.extend(generateComboTwo(between))
        combos.extend(generateComboThree(between))
        #print(combos)
        count += validComboCount(begin, end, combos)

        return count
    # need to calculate
    return -1

# numbers with a difference of three between them can't move
# only numbers between combinations can move
# a single number between blocks can't move
print("\n\n\n")
sequence = []
previous_pair = (0,0)
print("({})".format(real_begin))
combo_counts = []
i = 1
while i < len(numbers)-1:

    a = numbers[i]
    b = numbers[i+1]

    delta = b - a
    if delta == 3:
        i+=1
        # A and B are a fixed pair in the sequence
        #print(sequence)
        #print("_{}_ _{}_".format(a, b))
        
        begin = previous_pair[1]
        between = sequence
        end = a
        
        previous_pair = (a,b)

        # how many combinations between the end points?
        # simply try them all and see if they work
        combos = "?"
        print("_{}_ {} _{}_ ".format(begin, between, end), end="")
        
        combos = combinationsBetween(begin, between, end)
        print("combos:{}".format(combos))
        if combos > 0:
            combo_counts.append(combos)
        sequence =[]
    else:
        sequence.append(a)
    
    i +=1
 
print("({})".format(real_end))

print(combo_counts)

import math
## multiply together
total = 1
for c in combo_counts:
    total *= c # math.factorial(c)
print(total)

# n =
# r = 
# math.factorial(sum(combo_counts)) / (math.factorial(len(combo_counts)) * 

print("expect")
print(19208)

# tiny 8
# small 19208
# normal ?

# hmm must be missing something

# brute force tree that generates all the combinations via recursion might be faster
# could add all valid next numbers and then recurse for each
# function returns 1 or zero at the leaf when it reaches the end
# DFS over BFS to reduce memory consumption
# only 100 numbers so will only recurse 

def recursive(index, numbers, memo):
    #print(index)
    length = len(numbers)
    if index == (length -1):
        return 1

    if index in memo:
        return memo[index]

    total = 0
    current = numbers[index]
    # find possible new index
    i = index + 1
    
    while i < length and (current + 3) >= (numbers[i]):
        total += recursive(i, numbers, memo)
        i += 1

    memo[index] = total

    return total

print("test")
memo = dict()
count = recursive(0, numbers, memo)
print("count")
print(count)