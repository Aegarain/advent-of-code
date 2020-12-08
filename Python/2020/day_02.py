import re
input_file=open("day_02_input.txt")
input_text=input_file.read()

# nested list of policies and passwords
key = list(item.split(": ") for item in input_text.split("\n"))

# Part one

# number of valid passwords
valid = 0

for entry in key:
    # number of required letters
    letter_count = 0
    # dvides policy into list of minimum letters, maximum letters, and which letter
    div = re.split("-| ", entry[0])
    min = int(div[0])
    max = int(div[1])
    which = div[2]
    #split password string into list of letters
    password = list(entry[1])
    #checks if each letter is the one spcecified in the policy
    for letter in password:
        if letter == which:
            letter_count +=1
    #checks if letter count is within specified range
    if min <= letter_count <= max:
        valid +=1
print(valid)

#Part two

valid2 = 0

for entry in key:
    # dvides policy into 1st position, 2nd position, and which letter
    div = re.split("-| ", entry[0])
    pos1 = int(div[0]) - 1
    pos2 = int(div[1]) - 1
    which = div[2]
    #split password string into list of letters
    password = list(entry[1])
    # #checks if both letters are valid
    if (password[pos1] == which) + (password[pos2] == which) == 1:
        valid2 +=1
print(valid2)
