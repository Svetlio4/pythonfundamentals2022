import re

number_of_commands= int(input())
for command in range(number_of_commands):
    current_command = input()
    pattern = r'(!)([A-za-z]{3,})(\1{1})(:)([A-za-z]{8,})'
    result = re.findall(pattern, current_command)
    


