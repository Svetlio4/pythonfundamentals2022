text = input()

while text != 'end':
    text_reversed = ''
    for character in reversed(text):
        text_reversed += character
    print(text + ' = ' + text_reversed)
