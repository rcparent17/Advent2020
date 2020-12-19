numbers = []

with open("1.input") as inp:
    numbers.extend([int(x.strip()) for x in inp])

a = numbers[0]
b = numbers[1]

solFound = a + b == 2020

if not solFound:
    for i in range(2, len(numbers)):
        a = numbers[i]
        for j in range(i + 1, len(numbers)):
            b = numbers[j]
            solFound = a + b == 2020
            if solFound:
                break
        if solFound:
            break

print("solution:  the 2 numbers are {} and {}, and the result is {}".format(a, b, str(a * b)))
