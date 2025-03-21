correct_password = "1234"

user_input = input("Enter your password: ")

while user_input != correct_password:
    print("Incorrect password Try again")
    user_input = input("Enter your password: ")

print("Correct password You have successfully logged in")