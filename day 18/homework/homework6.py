fruits = ["apple", "banana", "mango", "kiwi", "peach"]
print("Current list:", fruits)

index = int(input("Enter the index of the fruit you want to remove: "))

if 0 <= index < len(fruits):
    del fruits[index]
    print("Updated list:", fruits)
else:
    print("Invalid index!")