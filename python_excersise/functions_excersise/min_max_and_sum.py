numbers = input().split()
sorted_numbers = []

for num in numbers:
    sorted_numbers.append(sorted(int(num)))

print(sorted_numbers)

