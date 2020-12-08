input_file = open("day_03_input.txt")
input_text = input_file.read()

forest = list(list(x) for x in input_text.split("\n"))

def find_cell(x, y, grid):
    width = len(grid[0])
    x = x % width
    pos = (grid[y])[x]
    return(pos)


def toboggan(velx, vely, grid):
    posx = 0
    posy = 0
    height = len(grid)
    trees = 0
    while posy < height:
        current_cell = find_cell(posx,posy,grid)
        if current_cell == "#":
            trees += 1
        posx += velx
        posy += vely
    return trees

part_one = toboggan(3,1,forest)
print(part_one)

slope_list = ((1,1),(3,1),(5,1),(7,1),(1,2))

part_two = 1
for slope in slope_list:
    part_two = part_two * toboggan(slope[0], slope[1], forest)

print(part_two)
