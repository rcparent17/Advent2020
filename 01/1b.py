numbers = []

with open("1.input") as inp:
    numbers.extend([int(x.strip()) for x in inp])

a = numbers[0]
b = numbers[1]
c = numbers[2]

solFound = a + b + c == 2020

if not solFound:
    for i in range(3, len(numbers)):
        a = numbers[i]
        for j in range(i + 1, len(numbers)):
            b = numbers[j]
            for k in range(j + 1, len(numbers)):
                c = numbers[k]
                solFound = a + b + c == 2020
                if solFound:
                    break
            if solFound:
                break
        if solFound:
            break

print("solution:  the 3 numbers are {}, {}, and {}, and the result is {}".format(a, b, c, str(a * b * c)))
