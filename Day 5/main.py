import math



def parse_file(inputFile):
    f = open(f"Day 5/{inputFile}", "r")
    codes = f.read().split("\n")
    
    return codes


def calc_max_val(list):
    high = 0

    for i in list:
        if i > high:
            high = i

    return high


def decode_code(code):
    fb = code[:7]
    rl = code[7::]
    row = [0, 127]
    col = [0, 7]


    for i in fb:
        if i == "F":
            row[1] = math.floor((row[0] + row[1]) / 2)
        elif i == "B":
            row[0] = math.ceil((row[0] + row[1]) / 2)
    
    for i in rl:
        if i == "L":
            col[1] = math.floor((col[0] + col[1]) / 2)
        elif i == "R":
            col[0] = math.ceil((col[0] + col[1]) / 2)


    return row[0] * 8 + col[1]


def main():
    codes = parse_file("input.txt")
    seat_IDs = []

    for code in codes:
        seat_IDs.append(decode_code(code))
    
    highest = calc_max_val(seat_IDs)

    print(highest)


main()
