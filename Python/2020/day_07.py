import re
input_file = open("day_07_input.txt")
input_text = input_file.read()

input = dict(x.split("s contain ") for x in input_text.split("\n"))


#Part 1
dead_end = set(())
shiny_gold = set(())

def find_child_bags(bag):
    children = re.sub(r'\d ', '', input[bag])
    children = re.sub(r'bags', 'bag', children)
    children = re.sub(r'\.', '', children)
    children = children.split(', ')
    for x in children:
        if x == "no other bag":
            dead_end.add(bag)
        elif x == "shiny gold bag":
            shiny_gold.add(bag)
            return True
        else:
            if find_child_bags(x):
                shiny_gold.add(bag)
                return True

for x in input:
    find_child_bags(x)

print(len(shiny_gold))


#Part 2

def count_child_bags(bag):
    children = input[bag]
    children = re.sub(r'bags', 'bag', children)
    children = re.sub(r'\.', '', children)
    children = children.split(', ')
    for x in children:
        global total_count
        if x != "no other bag":
            child = ""
            total_count += int(x[0])
            child = x[2:]
            for y in range(int(x[0])):
                count_child_bags(child)

total_count = 0
count_child_bags("shiny gold bag")
print(total_count)
