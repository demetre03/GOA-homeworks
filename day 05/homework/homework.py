# 1. ვქმნით ცვლადს სადაც ვინახავთ პაროლს
password = "deme32008911"

# 2. ვთხოვთ მომხმარებელს შეიყვანოს პაროლი
user_input = input("Enter the password: ")

# 3. ვამოწმებთ სწორია თუ არა მომხმარებლის შეყვანილი პაროლი
if user_input == password:
    print("access granted")
else:
    print("access denied")