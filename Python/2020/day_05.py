input_file = open("day_05_example.txt")
input_text = input_file.read()

boarding_passes = input_text.split("\n")
boarding_passes.pop()
highest_ID = 0
def read(pass_text):
    row = range(0,128)
    column = range(0,8)
    for x in range(8):
        row_len = int(len(row))
        mid = int(row_len/2)
        char = pass_text[x]
        # print("Midpoint is", mid)
        if char == "F":
            # print("Taking lower half")
            # print("Possible rows were", row)
            row = row[0:mid]
            # print("Possible rows now are", row)
        elif char == "B":
            # print("Taking upper half")
            # print("Possible rows were", row)
            row = row[-mid:]
            # print("Possible rows now are", row)
    row = row[0]
    for x in range(7,10):
        column_len = int(len(column))
        mid = int(column_len/2)
        char = pass_text[x]
        # print("Midpoint is", mid)
        if char == "L":
            # print("Taking lower half")
            # print("Possible columns were", column)
            column = column[0:mid]
            # print("Possible columns now are", column)
        elif char == "R":
            # print("Taking upper half")
            # print("Possible columns were", column)
            column = column[-mid:]
            # print("Possible columns now are", column)
    column = column[0]
    seat_ID = row * 8 + column
    return seat_ID
ids =[]
for y in boarding_passes:
    id = read(y)
    ids.append(id)
    if id > highest_ID:
        highest_ID = id

ids.sort()
print(highest_ID)
for z in range(len(ids)-1):
    if int(ids[z]) + 1 != int(ids[z+1]):
        print(ids[z], ids[z+1])
