names = input("Input names: ")
for letter in names:
    if 65 <= ord(letter) <= 90:
        n = names.title()
        print(letter)


