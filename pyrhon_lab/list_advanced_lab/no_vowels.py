text = input()

vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E' ,'I']
no_vowels = ''.join([ch for ch in text if ch not in vowels])
print(no_vowels)