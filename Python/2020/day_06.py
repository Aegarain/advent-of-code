input_file = open("day_06_input.txt")
input_text = input_file.read()

input = input_text.split("\n\n")


# Part one
unique1 = 0
def analyze1(group):
    unique_questions = set(())
    people = group.split("\n")
    for x in people:
        answers = list(x)
        for letter in answers:
            unique_questions.add(letter)
    return(len(unique_questions))

for group in input:
    unique1 += analyze1(group)

print(unique1)

# Part 2
unique2 = 0
def analyze2(group):
    unique_questions = set(())
    people = group.split("\n")
    # starts with the answers by the first person in the group
    for x in list(people[0]):
        unique_questions.add(x)
    # for each person
    for person in people:
        new_list = []
        # for each letter answered by everyone previously
        for letter in unique_questions:
            # check if this person answered yes as well
            if letter in person:
                # if not, remove it from the list of questions answered yes
                new_list.append(letter)
        unique_questions = new_list


    #returns number of questions answered yes by everyone
    return(len(unique_questions))

for group in input:
    unique2 += analyze2(group)

print(unique2)
