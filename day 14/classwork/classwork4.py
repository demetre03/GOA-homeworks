
numbers = [7, 7, 3, 7, 7]

numbers.sort()

if numbers[0] != numbers[1]:
    unique = numbers[0]
else:
    unique = numbers[-1]

print("Different number is:", unique)