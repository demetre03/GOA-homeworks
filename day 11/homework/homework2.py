secret_number = 5

while True:
    guess = int(input("Guess a number between 1-10: "))
    
    if guess == secret_number:
        print("Congrats You guessed it")
    else:
        print("that's Wrong try again!")