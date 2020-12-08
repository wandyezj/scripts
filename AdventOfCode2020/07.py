def readFile(file):
    f = open(file)
    data = f.read()
    f.close()
    return data



# there are no duplicate colors

# create dict of dicts

def parseRules(data):
    rules = dict()

    lines = data.strip().split("\n")

    for line in lines:
        pieces = line.split("bags contain")
        key = pieces[0].strip()
        
        values = []
        pieces = pieces[1].strip().split(" ")
        for i in range(0, len(pieces), 4):
            n = pieces[i]
            if n == "no":
                n = 0
            else:
                n = int(n)
            
                color = pieces[i+1] + " " + pieces[i+2]

                values.append((color, n))

        rules[key] = dict(values)

    return rules
    
def printRules(rules):
    # confirmed there are no duplicates
    for key, value in rules.items():
        print('{}'.format(key))
        for k, n in value.items():
            print("\t{} {}".format(n,k))
          

def bagsThatContainColor(rules, color):
    found = []
    for key, value in rules.items():
        if color in value:
            found.append(key)

    return found

# go down the complete tree
def bagsThatContainColorRecursive(rules, color):
    searched = set()
    new = bagsThatContainColor(rules, color)
    while len(new) > 0:
        searched = searched.union(new)
        search = []
        for color in new:
            found = bagsThatContainColor(rules, color)
            search.extend(found)
        new = set(search).difference(searched)

    return searched


def bagsInsideBagColorRecursive(rules, color):
    # recursively call itself for each bag down the tree and multiply by the count of those bags
    total = 1
    for color, n in rules[color].items():
        inside = bagsInsideBagColorRecursive(rules, color)
        total += n * inside

    return total
    

data = readFile("07.input.txt")

rules = parseRules(data)

print("Part1")
colors = bagsThatContainColorRecursive(rules, "shiny gold")
#print(colors)
print(len(colors))

print("Part 2")
# need to subtract 1 because does not count itself
count = bagsInsideBagColorRecursive(rules, "shiny gold") - 1
print(count)


