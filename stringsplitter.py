what = input("Enter an odd length string: ")
total_character_number = int(len(what))
middle_character_index = int((total_character_number - 1) / 2)
middle_character = what[middle_character_index]
first_half = what[0 : middle_character_index]
second_half = what[middle_character_index + 1 : total_character_number]

print("Middle character:", middle_character)
print("First half:", first_half)
print("Second half:", second_half)