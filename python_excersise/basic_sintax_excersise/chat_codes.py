number_of_send_messages = int(input())

for num in range(number_of_send_messages):
     number = int(input())
     if number == 88:
         print('Hello')
     elif number == 86:
          print('How are you?')
     elif number != 88 and number != 86 and number < 88:
          print('GREAT!')
     else:
          print('Bye.')