needed_experience = float(input())
count_of_battles = int(input())

gained_experience = 0
battles = 0
for current_battle in range(1, count_of_battles + 1):
    experience_per_battle = float(input())
    battles += 1
    gained_experience += experience_per_battle

    if current_battle % 3 == 0:
        gained_experience += experience_per_battle * 0.15

    if current_battle % 5 == 0:
        gained_experience -= experience_per_battle * 0.1

    if current_battle % 15 == 0:
        gained_experience += experience_per_battle * 0.05

    if gained_experience >= needed_experience:
        break

experience_left = needed_experience - gained_experience
if gained_experience >= needed_experience:
    print(f"Player successfully collected his needed experience for {battles} battles.")
else:
    print(f"Player was not able to collect the needed experience, {experience_left:.2f} more needed.")

