
number = "08"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip()

data = read_file(file)

'''
 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

Number  Segments    Single  Signal
0       6                   abc efg
1       2           yes       c  f 
2       5                   a cde g
3       5                   a cd fg
4       4           yes      bcd f 
5       5                   ab d fg
6       6                   ab defg
7       3           yes     a c  f 
8       7           yes     abcdefg
9       6                   abcd fg

segments -> number

2 -> 1
3 -> 7
4 -> 4
5 -> 2,3,5
6 -> 0,6,9
7 -> 8

How to decode each signal?

segments    reveal
2           cf

cf - the letters in the 1 (only 2 segment)
a - the letter not in 7 (only 3 segment)
c - shows up in every number except 6 (a 6 segment without one of the letters in the 2 segment)

# derive signals with rules and sets

cf = 2 segment
acf = 3 segment
bcdf = 4 segment
a = acf - cf
bc = bcdf - cf
df = bcdf - bc
d = df - cf
f = df - d
c = bc - cf
b = bc - c

abcdf = a + b + c + d + f

g = 6 segment - abcdf
eg = 6 segment - abcdf

e = eg - g

abcd fg + ab defg + abc efg

e
g

# 


create complete set of digits and match to values can sort and match with map

look up each value in the map and put together and add to total

'''

def splitter(line):
    signals, values = line.split(" | ")
    signals = signals.split()
    #signals.sort()
    values = values.split()
    #values.sort()
    return (signals, values)

lines = list(map(splitter, data.split("\n")))

print("")
print("Part 1")
# count segments
total = 0
for signals, values in lines:
    lengths = list(map(lambda x: len(x), values))

    ones = lengths.count(2)
    sevens = lengths.count(3)
    fours = lengths.count(4)
    eights = lengths.count(7)

    total += ones + sevens + fours + eights

print(total)


print("")
print("Part 2")

'''
Also know that each number is represented at least once in each piece of input

Possible to brute force simply try all combinations of signals to see what fits? Check validity of signals against each number.
8! = 40320 to try and 200 inputs = 8064000 brute force able.

But can also limit potential options for each letter

each letter maps to only one other letter

initially each input letter could map to any of the outputs

but when a single 

'''

# count segments
total = 0
for signals, values in lines:
    

    # segments
    # proof that each number is represented
    #l = list(map(lambda x: len(x), signals))
    #counts = list(map(lambda x : l.count(x), [2,3,4,5,6,7]))
    #print(counts)

    s2 = None
    s3 = None
    s4 = None
    s5s = []
    s6s = []
    s7 = None

    for s in signals:
        size = len(s)
        v = set(list(s))
        if size == 2:
            s2 = v
        elif size == 3:
            s3 = v
        elif size == 4:
            s4 = v
        elif size == 5:
            s5s.append(v)
        elif size == 6:
            s6s.append(v)
        elif size == 7:
            s7 = v

    cf = s2
    acf = s3
    bcdf = s4
    abcdefg = s7
    a = acf - cf
    bd = bcdf - cf
    aeg = abcdefg - bcdf
    eg = aeg - a

    b = None
    # abc efg
    # ab defg
    # abcd fg
    for s in s6s:

        find_b = (s - aeg) - cf
        if len(find_b) == 1:
            b = find_b
        pass

    d = bd - b

    g = None
    # a cde g
    # a cd fg
    # ab d fg
    for s in s5s:

        find_g = s - (a | cf | d)
        if len(find_g) == 1:
            g = find_g

    e = eg - g

    # split cf
    c = None
    # a cde g
    # a cd fg
    # ab d fg
    for s in s5s:

        find_c = s - (a | d | e | g)
        if len(find_c) == 1:
            c = find_c

    f = cf - c

    # now have the correct mapping of all segments

    # map segments to numbers
    a,b,c,d,e,f,g = list(map(lambda x: list(x), [a,b,c,d,e,f,g]))
    #print([a,b,c,d,e,f,g])
    a,b,c,d,e,f,g = list(map(lambda x: x[0], [a,b,c,d,e,f,g]))


    # n0 = a + b + c + e + f + g
    # n1 = c + f
    # n2 = a + c + d + e + g
    # n3 = a + c + d + f + g
    # n4 = b + c + d + f
    # n5 = a + b + d + f + g
    # n6 = a + b + d + e + f + g
    # n7 = a + c + f
    # n8 = a + b + c + d + e + f + g
    # n9 = a + b + c + d + f + g

    n0 = [a, b, c, e, f, g]
    n1 = [c, f]
    n2 = [a, c, d, e, g]
    n3 = [a, c, d, f, g]
    n4 = [b, c, d, f]
    n5 = [a, b, d, f, g]
    n6 = [a, b, d, e, f, g]
    n7 = [a, c, f]
    n8 = [a, b, c, d, e, f, g]
    n9 = [a, b, c, d, f, g]

    nx = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]
    for n in nx:
        n.sort()

    nx = list(map(lambda x: "".join(x), nx))

    #print(nx)
    values = list(map(list, values))
    for v in values:
        v.sort()
    values = list(map(lambda x: "".join(x), values))
    #print(nx)
    #print(values)
    numbers = list(map(lambda x: nx.index(x), values))
    numbers = list(map(lambda x: str(x), numbers))
    number = int("".join(numbers))
    #print(number)
    total += number

print(total)


