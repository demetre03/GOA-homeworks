correct_password = "demetre123"

while True:
    password = input("enter password: ")
     

    if password == correct_password:
        print("you logged in successfully.")
        break
    else:
        print("you entered incorrect password.")

