year = int(input())
next_happy_year_condition = False

while not next_happy_year_condition:
    year +=1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    next_happy_year_condition = len(set_year) == len(str(year))

print(year)