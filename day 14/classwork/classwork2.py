names = []

for i in range(5):
    name = input("Please enter name: ")
    names.append(name)


for name in names:
    if len(name) > 5:
        print(name)
    else:
        print("name < 5")