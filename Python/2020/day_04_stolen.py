from collections import Counter
import re

with open("day_04_input.txt") as f:
    passports = f.read().split("\n\n")

def check(pass_dict):

    valid = True

    num_limits= {
            'byr': (1920,2002),
            'iyr': (2010, 2020),
            'eyr': (2020,2030),
            'hgt':{
                'cm': (150,193),
                'in': (59, 76)
                }
            }

    reg_limits = {
            'hcl': re.compile('^#[0-9a-f]{6}$'),
            'ecl': re.compile('^(amb|blu|brn|gry|grn|hzl|oth){1}$'),
            'pid': re.compile('(\d{9}(?!\S))')
            }

    for key, val in pass_dict.items():

        if 'yr' in key:
            num = int(pass_dict[key])
            valid_nums = num_limits[key]
            valid = (num >= valid_nums[0] and  num <= valid_nums[1])

        elif 'hgt' in key and ('in' in pass_dict[key] or 'cm' in pass_dict[key]):
            num = int(pass_dict[key][0:-2])
            valid_nums = num_limits[key][pass_dict[key][-2:]]
            valid =  num >= valid_nums[0] and num <= valid_nums[1]

        elif 'cl' in key or 'pid' in key:
            valid = bool(reg_limits[key].match(pass_dict[key]))

        if not valid:
            #print(key, pass_dict[key])
            return valid

    return valid


count1=0
count2=0
for passport in passports:

    fl = Counter(passport)[':']

    if fl == 8 or (fl == 7 and 'cid' not in passport):
        count1+=1

        passport = passport.replace('\n', ' ')

        fields = dict(x.split(':') for x in passport.split(' '))
        if check(fields):
            count2+=1

print(f"Valid passports by field", count1)
print(f"Valid passports by data", count2)
