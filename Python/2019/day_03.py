input_file=open("day_03_example.txt")
input_txt=input_file.read()

data = [list(]item.split(",") for item in input_txt.split("\n")]

wire1 = data[0]
wire2 = data[1]

def plot(wire):
    for direction in wire
