secret_number = 4
guess = int(input("guess number between 1 and 10: "))

if guess == secret_number:
    print("congrats you guessed it")
else:
    print("sorry number is incorrect, correct number was", secret_number )