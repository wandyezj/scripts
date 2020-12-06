def readFileLines(file):
    f = open(file)
    data = f.read()
    f.close()
    lines = data.strip().split("\n")
    return lines

lines = readFileLines("05.input.txt")

#print(lines)

def binaryLocationNumber(text, lower, upper, max_low, max_high):
    low = max_low
    high = max_high
    middle = (high + low) //2
    for c in text:
        
        mid = (high + low) //2
        if c == upper:
            middle = mid + 1
            low = middle
        elif c == lower:
            middle = mid
            high = middle
        else:
            # ignore don't count
            continue
        #print('{} {} {} {}'.format(c, low, high, middle))

    return middle


def decodeSeatN(seat):

    # go through the seat
    #seat_row = seat[:-2]
    #seat_column = seat[-2:]

    row = binaryLocationNumber(seat, "F", "B", 0, 127)
    column = binaryLocationNumber(seat, "L", "R", 0, 7)
    
    n = row * 8 + column
    #print('row {} column {} n {}'.format(row, column, n))

    return n

# tests

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

numbers = []
for seat in lines:
    n = decodeSeatN(seat)
    numbers.append(n)

numbers.sort()

#print(numbers)
print('Part 1')
highest = numbers[-1]
print(highest)

print('Part 2')

lowest = numbers[0]

# not the most elegant
missing = -1
for i in range(lowest, highest +1):
    if i in numbers:
        #print('{}'.format(i))
        pass
    else:
        #print('{} missing'.format(i))
        missing = i
print(missing)

