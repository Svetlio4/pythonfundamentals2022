product = input()
number_of_products = int(input())
total_sum = 0

if product == 'coffee':
    sum = number_of_products * 1.50
    total_sum += sum
elif product == "water":
    sum = number_of_products * 1
    total_sum += sum
elif product == 'coke':
    sum = number_of_products * 1.40
    total_sum += sum
elif product == 'snacks':
    sum = number_of_products * 2
    total_sum += sum

print(f'{total_sum:.2f}')
