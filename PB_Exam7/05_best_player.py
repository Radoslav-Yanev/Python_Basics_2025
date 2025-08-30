import sys

most_goals = - sys.maxsize
best_player = ""

while True:
    player_name = input()

    if player_name == "END":
        break

    goals_count = int(input())

    if goals_count > most_goals:
        most_goals = goals_count
        best_player = player_name

    if goals_count >= 10:
        break

print(f"{best_player} is the best player!")

if most_goals >= 3:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")

else:
    print(f"He has scored {most_goals} goals.")

