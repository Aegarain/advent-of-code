input_file = open("day_10_input.txt")
input_text = input_file.read()

input = input_text.split("\n")

for x in input:
    input[input.index(x)] = int(x)

input.append(0)
input.sort()
print(input)


def difference(list, position):
    return int(list[position]) - int(list[(position-1)])

def chain():
    ones = 0
    threes = 1
    for x in range(1, len(input)):
        diff = difference(input, x)
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
    print(ones * threes)

chain()
