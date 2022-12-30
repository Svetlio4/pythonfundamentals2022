quantity_food_in_grams = float(input()) * 1000
quantity_hay_in_grams = float(input()) * 1000
quantity_cover_in_grams = float(input()) * 1000
guinea_s_weight_in_kilograms = float(input()) * 1000

flag = False

for day in range(1, 31):
    quantity_food_in_grams -= 300

    if day % 2 == 0 :
        quantity_hay_in_grams -= quantity_food_in_grams * 0.05

    if day % 3 == 0:
        quantity_cover_in_grams -= guinea_s_weight_in_kilograms / 3

    if quantity_food_in_grams <= 0 or quantity_hay_in_grams <= 0 or quantity_cover_in_grams <= 0:
        flag = True
        break

if not flag :
    food, hay, cover = quantity_food_in_grams / 1000, quantity_hay_in_grams /1000, quantity_cover_in_grams / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print(f'Merry must go to the pet store!')
