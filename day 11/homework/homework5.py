numbers = (10, 20, 30, 40, 50, 60)
total = 0

for i in range(0, len(numbers), 2):
    total += numbers[i]

print("Sum of index numbers:", total)