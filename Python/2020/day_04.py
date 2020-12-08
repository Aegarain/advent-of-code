input_file = open("day_04_input.txt")
input_text = input_file.read()

input = input_text.split("\n\n")

fields = ("byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:",)
def valid(passport):
    valid_fields = 0
    for field in fields:
        if field in passport:
            valid_fields +=1
    if valid_fields == 7:
        return True
    else:
        return False

def validate_batch(batch):
    valid_passports = 0
    for passport in batch:
        if valid(passport):
            valid_passports +=1
    return valid_passports

print(validate_batch(input))
