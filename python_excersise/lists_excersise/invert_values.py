numbers = input().split()
oposite_numbers = []

for element in numbers:
    current_number = -int(element)
    oposite_numbers.append(current_number)

print(oposite_numbers)