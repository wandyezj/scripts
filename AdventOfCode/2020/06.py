def readFile(file):
    f = open(file)
    data = f.read()
    f.close()
    return data


data = readFile("06.input.txt")
groups = data.strip().split("\n\n")

total =0

same = 0

# knew they were goint to ask for groups of answers
for group in groups:
    answers = group.split("\n")
    combined = set()

    #questions = string.ascii_lowercase
    totals = [0 for i in range(26)]
    #print(totals)
    for answer in answers:
        for q in answer:
            index = ord(q) - ord('a')
            totals[index] += 1
        
        s = set(list(answer.strip()))
        combined = combined.union(s)
    
    count = len(combined)
    total += count
    #print(len(combined))

    #print(totals)
    
    expect = len(answers)
    for i in totals:
        if i == expect:
            same += 1
        

print("Part 1")
print(total)

print("Part 2")
print(same)
