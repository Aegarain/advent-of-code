import re
input_file = open("day_09_example.txt")
input_text = input_file.read()

list = list(int(x) for x in input_text.split("\n"))

preamble = 5

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

invalid = XMAS(list, preamble)
print(invalid)

def find_sum(input):
    start = 0
    for x in input:
        dummy_list = input.copy()
        dummy_list = dummy_list[x+1:]
