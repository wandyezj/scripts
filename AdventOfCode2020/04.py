# this particular program would be much more elegant in TypeScript

def readFile(file):
    f = open(file)
    data = f.read()
    f.close()
    return data


data = readFile("04.input.txt")
raw_records = data.strip().split("\n\n")
# put records in standard format all one line
records = []
for raw in raw_records:
    pieces = raw.strip().split("\n")
    same = " " + " ".join(pieces)
    records.append(same)

#print(records)

fields = '''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
'''
# ignore the cid field
# cid (Country ID)

expected = []
for line in fields.strip().split("\n"):
    name = line.split(" ")[0].strip()
    expected.append(" " + name + ":")

# go through the records and make sure all fields are present

def hasAllExpected(s, expected):
    for expect in expected:
        count = record.count(expect)
        if count == 0:
            return False
    return True

records_with_required_fields = []
for record in records:
    if hasAllExpected(record, expected):
        records_with_required_fields.append(record)
print("Part 1")
print("valid records")
print(len(records_with_required_fields))

print()
print("Part 2")
# go through valid records and parse out the things from them

def in_range(value, minimum, maximum):
    n = int(value)
    return  n >= minimum and n <= maximum

def valid_four_digit(value, minimum, maximum):
    return len(value) == 4 and in_range(value, minimum, maximum)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def valid_byr(value):
    return valid_four_digit(value, 1920, 2002)

# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def valid_iyr(value):
    return valid_four_digit(value, 2010, 2020)

# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def valid_eyr(value):
    return valid_four_digit(value, 2020, 2030)

# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
def valid_hgt(value):
    n = value[0:-2]
    if value.endswith('cm'):
        return in_range(n, 150, 193)
    if value.endswith('in'):
        return in_range(n, 59, 76)

    return False

# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def valid_hcl(value):
    # far easier to do with regex in TypeScript
    if len(value) == 7 and value[0] == '#':
        for c in value[1:]:
            if not (c in '0123456789abcdef'):
                return False
        return True

    return False

# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def valid_ecl(value):
    possible = 'amb blu brn gry grn hzl oth'.split(" ")
    return value in possible

# pid (Passport ID) - a nine-digit number, including leading zeroes.
def valid_pid(value):
    return len(value) == 9 and value.isdigit()

# cid (Country ID) - ignored, missing or not
def valid_cid(value):
    return True

validators = {
    'byr':valid_byr, 
    'iyr': valid_iyr,
    'eyr': valid_eyr,
    'hgt': valid_hgt,
    'hcl': valid_hcl,
    'ecl': valid_ecl,
    'pid': valid_pid,
    'cid': valid_cid,
};


def fieldsValid(record):
    fields = record.strip().split(" ")
    # go over all fields and validate each one
    for field in fields:
        key, value = field.split(":")
        if key in validators:
            if not validators[key](value):
                #print('fail {} {}'.format(key, value))
                return False
    return True


valid = 0
for record in records_with_required_fields:
    if fieldsValid(record):
        valid += 1
print('valid records')
print(valid)

