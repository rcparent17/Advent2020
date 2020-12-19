import re

passports = []
validPassports = 0

neededFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open("4.input", "r") as inp:
    passportBlocks = ("".join(inp.readlines())).split("\n\n")

    for i in range(len(passportBlocks)):
        while "\n" in passportBlocks[i]:
            passportBlocks[i] = passportBlocks[i].replace("\n", " ")
        
        passportBlocks[i] = passportBlocks[i].strip()

        currentBlock = dict()

        for field in passportBlocks[i].split():
            currentBlock[field.split(":")[0]] = field.split(":")[1]
        passports.append(currentBlock)

def eyeValid(eye):
    return eye in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def yearValid(year, low, high):
    if year.isnumeric():
        return len(year) == 4 and int(year) >= low and int(year) <= high
    return False

def heightValid(height):
    result = True
    if "cm" in height:
        height = int(height.replace("cm", ""))
        if height < 150 or height > 193:
            result = False
    elif "in" in height:
        height = int(height.replace("in", ""))
        if height < 59 or height > 76:
            result = False
    else:
        result = False
    return result

def validate(field, value):
    switch = {
            "byr": yearValid(value, 1920, 2002),
            "iyr": yearValid(value, 2010, 2020),
            "eyr": yearValid(value, 2020, 2030),
            "hgt": heightValid(value),
            "hcl": re.match("#[a-f0-9]{6}", value),
            "ecl": eyeValid(value),
            "pid": len(value) == 9 and value.isnumeric(),
            "cid": True,
    }
    return switch.get(field, False)

for passport in passports:
    isValid = True
    for field in neededFields:
        if not field in passport.keys():
            isValid = False
            break
        if not validate(field, passport[field]):
            isValid = False
            break
    if isValid:
        validPassports += 1

print("Valid passports: " + str(validPassports))
