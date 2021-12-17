
number = "16"
file_sample = number + ".data.sample.txt"
file = number + ".data.txt"

def read_file(file):
    f = open(file)
    data = f.read()
    f.close()
    return data.strip()

data = read_file(file_sample)

'''
packet comes in hexdecimal
which needs to be translated to bits

Every packet

Standard header
    3 bits - package version
    3 bits - type id

id 100 - literal value
    following is padded with 0s so it is a multiple of 4 bits
    {prefix}{4 bits}
    each group prefixed with 1 until last which is prefixed with 0

if other - operator
    1 bit - length type
        0 - 15 bits represent total length of the subpackets within the packet
        1 - 11 bits represent number of subpackets within the packet
    subpackets


'''

hex_to_bits = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111",
}


def parse_bits_from_hex(hex):
    s = ""
    for c in hex:
        s += hex_to_bits[c]

    return s


def parse_packets(bits, packet_start):
    # return all packets in the order found
    print(bits)

    # have to figure out where the packet ends
    packet_end = None

    packet_version_bits = bits[packet_start : packet_start + 3]
    packet_version = int(packet_version_bits, 2)
    packet_type_bits = bits[packet_start + 3: packet_start + 6]

    print("version bits: {}".format(packet_version_bits))
    print("type bits: {}".format(packet_type_bits))

    packet_literal_bits = None
    packet_literal = None
    packet_subpackets = None

    if packet_type_bits == "100":
        # literal packet
        start_index = packet_start + 6
        index = start_index

        packet_literal_bits = ""

        while True:
            segment = bits[index: index + 5]
            print(segment)
            packet_literal_bits += segment[1:]

            control_bit = bits[index]
            if control_bit == "0":
                break

            index += 5

        packet_end = index + 4 # last bit in packet

        packet_literal = int(packet_literal_bits, 2)

    else:
        packet_subpackets = []
        packet_length_type_bit = bits[packet_start + 6]
        print("length type ID bits: {}".format(packet_length_type_bit))
        if packet_length_type_bit == "0":
            # If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
            packet_subpacket_length_literal_bits = bits[packet_start + 7:packet_start + 7 + 15]
            
            packet_subpacket_length_literal = int(packet_subpacket_length_literal_bits, 2)
            subpacket_start = packet_start + 7 + 15
            # parse each packet and continue to parse packets until a packet end equals or exceeds the bits
            index = subpacket_start
            while index < subpacket_start + packet_subpacket_length_literal:
                subpacket = parse_packets(bits, index)
                packet_subpackets.append(subpacket)
                index = subpacket["end_bit"]
            packet_end = index

        else:
            #If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
            packet_subpacket_count_literal_bits = bits[packet_start + 7:packet_start + 7 + 11]
            packet_subpacket_count_literal = int(packet_subpacket_count_literal_bits, 2)
            subpacket_start = packet_start + 7 + 11
            # parse n packets each starting off where the last ended
            index = subpacket_start
            for i in range(packet_subpacket_count_literal):
                subpacket = parse_packets(bits, index)
                packet_subpackets.append(subpacket)
                index = subpacket["end_bit"]
            packet_end = index





    packet = {
        # can calculate length from start and end
        "start_bit": packet_start,
        "end_bit": packet_end,
        "version_bits": packet_version_bits,
        "version": packet_version,
        "type_bits": packet_type_bits,
        "literal_bits": packet_literal_bits,
        "literal": packet_literal,
        "subpackets": packet_subpackets,
    }

    return packet


def parse_packet_hex(hex):
    print(hex)
    bits = parse_bits_from_hex(hex)
    print(bits)
    packets = parse_packets(bits, 0)
    return packets

# string of bits
data = "EE00D40C823060"
data_bits = "11101110000000001101010000001100100000100011000001100000"
bits = parse_bits_from_hex(data)
# print(data_bits)
# print(bits)

print("\n\nA")
print(parse_packets("110100101111111000101000", 0))

print("\n\nB")
print(parse_packet_hex("38006F45291200"))



print("")
print("Part 1")


print("")
print("Part 2")


