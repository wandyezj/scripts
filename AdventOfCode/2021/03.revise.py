number = "03"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file_lines(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip().split("\n")

numbers = read_file_lines(file)


def count_ones(numbers, index):
    return len(list(filter(lambda x : x[index] == "1", numbers)))

def flip(n):
    return "".join(list(map(lambda x: "1" if x == "0" else "0", list(n))))

print("Part 1")

gamma_bin = ""
for i in range(len(numbers[0])):

    count = count_ones(numbers, i)
    ones = count
    zeros = len(numbers) - count

    gamma_bin += "1" if ones > zeros else "0"

gamma = int(gamma_bin, 2)
epsilon = int(flip(gamma_bin), 2)

print(gamma * epsilon)

print("Part 2")

def rating(numbers, prefix_builder, prefix= ""):

    numbers = list(filter(lambda x: x.startswith(prefix), numbers))
    #print(prefix)
    #print(numbers)
    if len(numbers) <= 1:
        return numbers[0]

    i = len(prefix)

    count = count_ones(numbers, i)
    ones = count
    zeros = len(numbers) - count

    prefix += prefix_builder(ones,zeros)

    return rating(numbers, prefix_builder, prefix)


generator_rating = rating(numbers, lambda ones, zeros: "1" if ones >= zeros else "0")
#print(generator_rating)

scrubber_rating = rating(numbers, lambda ones, zeros: "1" if ones < zeros else "0")
#print(scrubber_rating)

generator = int(generator_rating, 2)
scrubber = int(scrubber_rating, 2)

print(generator * scrubber)


