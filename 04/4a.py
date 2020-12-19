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

for passport in passports:
    isValid = True
    for field in neededFields:
        if not field in passport.keys():
            isValid = False
            break
    if isValid:
        validPassports += 1

print("Valid passports: " + str(validPassports))
