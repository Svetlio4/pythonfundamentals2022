activation_key = input()

while True:
    command = input().split('>>>')
    current_command = command[0]

    if current_command == "Generate":
        print(f"Your activation key is: {activation_key}")
        break
    elif current_command == 'Contains':
        if activation_key in command:
            print(f"{activation_key} contains {command}")
        else:
            print("Substring not found!")
    elif current_command == 'Flip':
        substring = command[1]
        start_index =
        index = (command[1])
        if substring in activation_key:


        print(activation_key)

    elif current_command == 'Slice':
        pass