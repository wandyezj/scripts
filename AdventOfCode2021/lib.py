# flip string of zeros and ones example: 1010 <-> 0101
def flip_bits(n):
    return "".join(list(map(lambda x: "1" if x == "0" else "0", list(n))))
