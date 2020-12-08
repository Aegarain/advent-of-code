from math import floor

input_file=open("day_01_input.txt")
input_txt=input_file.read()

masses = input_txt.split("\n")
print(masses)

fuel = 0
for mass in masses:
    iter = int(mass)
    while True:
        iter = floor(iter/3) - 2
        if iter > 0:
            fuel += iter
        else:
            break

print(fuel)
