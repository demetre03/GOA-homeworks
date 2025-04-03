def vowels(str):
    vowels = "aeiouAEIOU"
    str2 = ""
    for i in str:
        if i in vowels:
            str2 = str2 + i
    return str2 

print(vowels("demetre"))    