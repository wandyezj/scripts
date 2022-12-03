
number = "10"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip()

data = read_file(file)


lines = data.split("\n")

print("")
print("Part 1")

score = 0
for line in lines:

    tokens = list(line)

    stack = []

    points = 0
    for t in tokens:
        open_tokens = "([{<"
        close_tokens = ")]}>"
        points_tokens = [3, 57, 1197, 25137]
        index = open_tokens.find(t)
        if index >=0:
            stack.append(close_tokens[index])

        else:
            last = stack[-1]
            if last == t:
                stack.pop(-1)
            else:
                index = close_tokens.find(t)
                points = points_tokens[index]
                break
    score += points

print(score)

print("")
print("Part 2")

open_tokens = "([{<"
close_tokens = ")]}>"
points_tokens = [1, 2, 3, 4]

scores = []
for line in lines:

    tokens = list(line)

    stack = []

 
    good = True
    for t in tokens:

        index = open_tokens.find(t)
        if index >=0:
            stack.append(close_tokens[index])
        else:
            last = stack[-1]
            if last == t:
                stack.pop(-1)
            else:
                good = False

    # score
    
    if good:
        points = 0
        stack.reverse()
        #print("".join(stack))
        for v in stack:
            
            index = close_tokens.find(v)
            value = points_tokens[index]
            points *= 5
            points += value

        #print(points)
        scores.append(points)

scores.sort()
print(scores[len(scores)//2])

#print(score) # 287883076754 - too high


