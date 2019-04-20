s = """
wwbzdp

uqxrj

mwag

kmxbbyyqrtky

sseapiqp

tztkcqmkiezdh

bianvlqikhajx

vmlufy

goroauzilqshkfmnngffmw

ahpfwwnmvmomv

lnyfap

ofplaeufxbkfhjoouokmi

olwjimarcljgehpzuo

bzhhlqox

fqyqdkdxvifvtrnp

wiaugilwrmgdkclx

mulfy

zstrwmv

osolmmrofe

fdcfxibl

mb
""".strip();


import random

def shuffle(s):
    shuffled = list(s)
    random.shuffle(shuffled)
    return ''.join(shuffled)
    
import string
def randomize(s):
    return ''.join(string.ascii_lowercase[random.randint(0, 25)] for i in s)

l = s.split("\n")

c = []
for i in l:

    #print(randomize(i))
    #print(i)
    i = i.strip()
    if i:
        c.append(i)

# print(c)

columns = 3

rows = []
for row in range(0, len(c), columns):
    # print(i)
    items = []
    for column in range(0, columns):
        index = row + column
        item = c[index].strip()
        items.append(item)

    #print(items)
    rows.append(items)


# Adjust row order
for i in range(len(rows)):
    rows[i].reverse()


max_lens = []

for i in range(columns):
    max_lens.append(0)


for row in rows:
    for i in range(columns):
        m = len(row[i])
        if m > max_lens[i]:
            max_lens[i] = m

#print(max_lens)

under_row = []
for header in rows[0]:
    under_row.append("-" * len(header))

rows.insert(1, under_row)

for row in rows:
    adjusted_column = []
    for i in range(len(row)):
        adjusted_column.append(row[i].ljust(max_lens[i]))
        
    
    print(" | ".join(adjusted_column))

# Insert heading row



