numValid = 0
passwords = []

def verifyPassword(pw):
    global numValid
    letterCount = 0
    parts = pw.split()
    checkLetter = parts[1][0]
    minCount, maxCount = int(parts[0].split("-")[0]), int(parts[0].split("-")[1])
    for ch in parts[2]:
        if ch == checkLetter:
            letterCount += 1
    if letterCount >= minCount and letterCount <= maxCount:
        numValid += 1
        return True
    return False


with open("2.input", "r") as inp:
    passwords.extend([x.strip() for x in inp])

for pw in passwords:
    verifyPassword(pw)

print("Valid passwords: " + str(numValid))
