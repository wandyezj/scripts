def readFile(file):
    f = open(file)
    data = f.read()
    f.close()
    
    return data

# The problem simply describes binary

translate =  [
    ('F', '0'),
    ('B', '1'),
    ('L','0'),
    ('R','1')
    ]

def translateToBinary(data):
    for target, replacement in translate:
        data = data.replace(target, replacement)
    return data


def decodeSeatN(seat):
    binary = translateToBinary(seat)
    return int(binary, base=2)

# Test
def test(seat, expect):
    actual = decodeSeatN(seat)
    passes = actual == expect
    if not passes:
        print('{} {} {}'.format(passes, actual, expect, ))

cases = [('BFFFBBFRRR', 567), 
('FFFBBBFRRR', 119),
('BBFFBBFRLL', 820)]
for seat, expect in cases:
    test(seat, expect)

# Execute

# Find all seat numbers
data = readFile("05.input.txt")
seats = data.strip().split("\n")
numbers = []
for seat in seats:
    n = decodeSeatN(seat)
    numbers.append(n)

# order seat numbers ascending
numbers.sort()

# last seat is the highest number
highest = numbers[-1]

print('Part 1')
print(highest)


print('Part 2')
# expectation is a list of numbers that increases by one of each number
# note guarantees in the problem means there is only one missing seat
# find the number that is out of place
lowest = numbers[0]

current = lowest
for n in numbers:
    if n != current:
        print('missing' + str(current))
        break

    current += 1 



