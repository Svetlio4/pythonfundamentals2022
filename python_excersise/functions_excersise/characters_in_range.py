def collect_characters(first,second):
    characters = []
    for current_character in range(ord(first) +1, ord(second)):
        characters.append(chr(current_character))
    return characters



first_character = input()
second_character = input()
result = collect_characters(first_character,second_character)
print(' '.join(result))