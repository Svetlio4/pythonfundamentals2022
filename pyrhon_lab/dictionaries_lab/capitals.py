countries = input().split(', ')
capitals = input().split(', ')
final_result= {countries[index] : capitals[index] for index in range(len(capitals))}
for country, capital in final_result.items():
    print(f"{country} -> {capital}")
