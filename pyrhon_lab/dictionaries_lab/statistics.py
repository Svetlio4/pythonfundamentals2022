products = {}
command = input()
while command != "statistics":
    key, value = command.split(": ")
    if key not in products.keys():
        products[key] = 0
    products[key] += value
    command = input()
print("Products in stock:")
for product, quantity in products.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(int(s) for s in products.values())}')
