import re
input_file = open("day_09_input.txt")
input_text = input_file.read()

data = list(int(x) for x in input_text.split("\n"))

preamble = 25

def check_valid(number, range):
    Valid = False
    for x in range:
        if Valid:
            break
        for y in range:
            if y == x:
                break
            if y + x == number:
                Valid = True
                break
    return Valid


def XMAS(input, length):
    total_length = len(input) - length
    pos = int(length)
    while True:
        lower_bound = pos - length
        if not check_valid(input[pos],input[lower_bound:pos]):
            return input[pos]
            break
        else:
            pos +=1

invalid = XMAS(data, preamble)
print(invalid)

def find_sum(input):
    for x in input:
        start = input.index(x)
        dummy_list = input.copy()
        dummy_list = dummy_list[start+1:]
        for y in dummy_list:
            stop = input.index(y)
            set = input[start:stop]
            set.sort()
            if sum(set) > invalid:
                break
            elif sum(set) == invalid:
                return set[0] + set[-1]
                break

x = find_sum(data)
print(x)
