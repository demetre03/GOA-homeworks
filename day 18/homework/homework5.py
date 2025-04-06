my_list = ["apple", "banana", "orange", "kiwi", "grape"]

answer = input("Do you want to clear the list? (yes or no): ")

if answer.lower() == "yes":
    my_list.clear()
    print("The list has been cleared:", my_list)
else:
    print("The list remains as it was:", my_list)