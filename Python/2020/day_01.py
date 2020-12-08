txt = open("day_01_input.txt")

input = txt.read()
input_list = input.split("\n")
for number in input_list :
    for addend in input_list:
        collection = (int(number), int(addend))
        if sum(collection) == 2020:
            solution=int(number)*int(addend)
    input_list.remove(number)
print(solution)
solution_two = 0
input_list2 = input.split("\n")
for number in input_list2 :
    for addend in input_list2:
        for addend2 in input_list2:
            collection = (int(number), int(addend), int(addend2))
            if sum(collection) == 2020:
                solution2=int(number)*int(addend)*int(addend2)
    input_list2.remove(number)

print(solution2)
