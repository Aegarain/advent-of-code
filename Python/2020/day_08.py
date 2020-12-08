import copy
input_file = open("day_08_input.txt")
input_text = input_file.read()

input = list(x.split(" ") for x in input_text.split("\n"))


Part One
def run(tape):
    pos = 0
    acc = 0
    visited = set(())
    while True:
        instruct = tape[pos]
        if pos in visited:
            print(acc)
            break
        elif instruct[0] == "nop":
            visited.add(pos)
            pos += 1
        elif instruct[0] == "acc":
            visited.add(pos)
            acc += int(instruct[1])
            pos += 1
        elif instruct[0] == "jmp":
            visited.add(pos)
            pos += int(instruct[1])



#Part Two
# Runs through given tape, printing the accumulator value when the program runs an instructiona after the last instruction
def run2(tape):
    pos = 0
    acc = 0
    visited = set(())
    while True:
        if pos >= len(tape):
            print(acc)
            break
        else:
            instruct = tape[pos]
            if pos in visited:
                break
            elif instruct[0] == "nop":
                visited.add(pos)
                pos += 1
            elif instruct[0] == "acc":
                visited.add(pos)
                acc += int(instruct[1])
                pos += 1
            elif instruct[0] == "jmp":
                visited.add(pos)
                pos += int(instruct[1])

# For each instruction, changes jmp to nop or nop to jmp, and then runs through to check if that fixed the program
# Input is formated as (("instruction", "number"), ("instruction", "number"), ... ("instruction", "number"))
# So [['nop', '+0'], ['acc', '+1'], ['jmp', '+4'], ['acc', '+3'], ['jmp', '-3'], ['acc', '-99'], ['acc', '+1'], ['jmp', '-4'], ['acc', '+6']]
def correct(tape):
    for x in tape:
        index = tape.index(x)
        dummy = copy.deepcopy(tape)
        if tape[index][0] == "jmp":
            dummy[index][0] = "nop"
            run2(dummy)
        elif tape[index][0] == "nop":
            dummy[index][0] = "jmp"
            run2(dummy)
correct(input)
