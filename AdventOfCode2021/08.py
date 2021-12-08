
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

e
g

# 

derive sets to digits

'''

def splitter(line):
    signals, values = line.split(" | ")
    signals = signals.split()
    signals.sort()
    values = values.split()
    values.sort()
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
for signals, values in lines:
    l = list(map(lambda x: len(x), signals))

    # segments
    # proof that each number is represented
    #counts = list(map(lambda x : l.count(x), [2,3,4,5,6,7]))
    #print(counts)



#print(total)


