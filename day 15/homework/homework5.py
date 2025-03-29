def format_sentence(sentence):
    print("Lowercase:", sentence.lower())      
    print("Uppercase:", sentence.upper())      
    print("Capitalized:", sentence.capitalize())

user_input = input("Enter a sentence: ")

format_sentence(user_input)