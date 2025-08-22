STARTING_POINTS = 301

player_name = input()

successful_shots = 0
unsuccessful_shots = 0
multiplier = 0
is_winer = False

while True:
    area = input()

    if area == "Retire":
        break

    current_points = int(input())

    if area == "Single":
        multiplier = 1

    elif area == "Double":
        multiplier = 2

    elif area == "Triple":
        multiplier = 3

    total_points = (current_points * multiplier)

    if total_points > STARTING_POINTS:
        unsuccessful_shots += 1

    else:
        STARTING_POINTS -= total_points
        successful_shots += 1

    if STARTING_POINTS == 0:
        is_winer = True
        break

if is_winer:
    print(f"{player_name} won the leg with {successful_shots} shots.")
else:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")