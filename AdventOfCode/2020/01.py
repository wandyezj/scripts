
f = open("01.data.txt")
data = f.read()
f.close()


numbers = []
l = data.strip().split("\n")
for i in l:
    s = i.strip();
    #print(s)
    numbers.append(int(s))


#print(numbers)

def numbersThatAddToNumber(numbers, target):
    numbers.sort()
    count = len(numbers)
    for i in range(count):
        for t in range(i+1, count):
            #print(i, t)
            a = numbers[i]
            b = numbers[t]
            if a + b == target:
                return [a,b]

    return [-1,-1]

def numbersThatAddToNumberTriplet(numbers, target):
    numbers.sort()
    count = len(numbers)
    for i in range(count):
        for t in range(i+1, count):
            for p in range(t+1, count):
                #print(i, t)
                a = numbers[i]
                b = numbers[t]
                c = numbers[p]
                if a + b +c == target:
                    return [a,b, c]

    return [-1,-1, -1]

target = 2020
targets = numbersThatAddToNumber(numbers, target)
print(targets)
print(sum(targets))

# Part 1
if len(targets)==2 and sum(targets) == target:
    print("found pair")
    print(targets)
    print(sum(targets))
    print("answer")
    print(targets[0] * targets[1])


# Part 2
targets = numbersThatAddToNumberTriplet(numbers, target)
if len(targets)==3 and sum(targets) == target:
    print("found triplet")
    print(targets)
    print(sum(targets))
    print("answer")
    print(targets[0] * targets[1] * targets[2])

