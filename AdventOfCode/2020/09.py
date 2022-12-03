def readFile(file):
    f = open(file)
    data = f.read()
    f.close()
    return data

def readFileNumberList(file):
    data = readFile(file)
    lines = data.strip().split("\n")
    return list(map(int, lines))

# Solution is ugly, could have tracked array bounds and gone though each once 

def uniquePairsAdded(numbers):
    pairs = []
    for a in range(len(numbers)):
        for b in range(a + 1, len(numbers)):
            pairs.append(numbers[a] + numbers[b])

    return pairs


def firstNumberNotMultipleOfPreviousTwentyFive(numbers):

    previousTwentyFive = []

    for i in range(len(numbers)):
        n = numbers[i]

        if len(previousTwentyFive) >= 25:
            pairs = uniquePairsAdded(previousTwentyFive)
            if not n in pairs:
                return n
            # make room
            previousTwentyFive.pop(0)

        previousTwentyFive.append(n)


def contiguousRangeThatSumsToN(numbers, n):

    for i in range(len(numbers)):
        m = i + 1
        total = 0
        while m < len(numbers) and total < n:
            chunk = numbers[i:m]
            total = sum(chunk)
            if total == n:
                return chunk
            m +=1

    return []

numbers = readFileNumberList("09.input.txt")

print("Part 1")
first = firstNumberNotMultipleOfPreviousTwentyFive(numbers)
print(first)

print("Part 2")
contiguous = contiguousRangeThatSumsToN(numbers, first)
#print(contiguous)
high = max(contiguous)
low = min(contiguous)
weakness = high + low
print(weakness)