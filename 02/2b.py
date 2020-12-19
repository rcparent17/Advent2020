numValid = 0
passwords = []

def verifyPassword(pw):
    global numValid
    parts = pw.split()
    letterCount = 0
    checkLetter = parts[1][0]
    lowerBound, upperBound = int(parts[0].split("-")[0]) - 1, int(parts[0].split("-")[1]) - 1
    if (parts[2][lowerBound] == checkLetter) != (parts[2][upperBound] == checkLetter):
        numValid += 1
        return True
    return False


with open("2.input", "r") as inp:
    passwords.extend([x.strip() for x in inp])

for pw in passwords:
    verifyPassword(pw)

print("Valid passwords: " + str(numValid))
