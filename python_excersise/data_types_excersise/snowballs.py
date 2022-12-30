number_of_snowballs = int(input())

for snowball in range (number_of_snowballs):
    weight_of_snowball = int(input())
    time_needed = int(input())
    quality_of_snowball = int(input())

snowball_value = (weight_of_snowball / time_needed) ** quality_of_snowball
print(f"{weight_of_snowball} : {time_needed} = {snowball_value} ({quality_of_snowball})")