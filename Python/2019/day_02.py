from math import floor

input_file=open("day_02_input.txt")
input_txt=input_file.read()

tape = input_txt.split(",")

def read(pos):
    return int(tape[pos])

def write(pos, data):
    tape[pos] = data

def run():
    place = 0
    while True:
        mode = read(place)

        if mode == 99:
            break

        in1 = read(place+1)

        in2 = read(place+2)

        out3 = read(place+3)

        if mode == 1:
            write(out3, read(in1) + read(in2))
        elif mode == 2:
            write(out3, read(in1) * read(in2))
        place +=4

test = range(121)
iter = 0
for first in test:
    for second in test:
        tape = input_txt.split(",")
        tape[1] = first
        tape[2] = second
        run()
        if tape[0] == 19690720:
            print(first, second)
