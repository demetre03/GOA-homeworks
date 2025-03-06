num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 > num2:
    print(f"{num1} მეტია {num2}-ზე")
elif num1 < num2:
    print(f"{num2} მეტია {num1}-ზე")
else:
    print("ორივე რიცხვი ტოლია")
