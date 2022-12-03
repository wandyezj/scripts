file = "01.data.txt"

f = open(file)
data = f.read()
f.close()

lines = data.split("\n")

readings = []
for line in lines:
    readings.append(int(line))

print(readings)

# count all the increases

# have a counter
counter = 0

# each time number icreases increment the counter

for i in range(1, len(readings)):
    previous = readings[i - 1]
    current = readings[i]

    # compare previous to current

    is_greater = current > previous
    if is_greater:
        counter += 1

    #print("{} {} {} {}".format(i, previous, current, is_greater))
    
print("Part 1")
print(counter)




# have a counter
counter = 0

for i in range(3, len(readings)):
    a = readings[i - 3]
    b = readings[i - 2]
    c = readings[i - 1]
    d = readings[i]
    
    previous = a + b + c
    current = b + c + d

    # compare previous to current

    is_greater = current > previous
    if is_greater:
        counter += 1

    #print("{} {} {} {}".format(i, previous, current, is_greater))
    
print("Part 2")
print(counter)



