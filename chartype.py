character = input("Enter a character: ")
if (character.islower()):
    print(character, "is a lower case letter.")
elif (character.isupper()):
    print(character, "is an upper case letter.")
elif (character.isdigit()):
    print(character, "is a digit.")
else:
    print(character, "is a non-alphanumeric character.")
  