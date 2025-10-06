def all_the_character(first_character, second_character):
    characters = []
    for current_character in range(ord(first_character) + 1, ord(second_character)):
        characters.append(chr(current_character))
    return characters


first_character = input()
second_character = input()
result = all_the_character(first_character, second_character)
print(" ".join(result))
