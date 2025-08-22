win_count = 0
lose_count = 0
total_matches = 0

while True:
    tournament_name = input()

    if tournament_name == "End of tournaments":
        break

    match_count = int(input())
    match_number = 0

    for _ in range(match_count):
        desi_team_points = int(input())
        enemy_team_points = int(input())

        match_number += 1

        if desi_team_points > enemy_team_points:
            print(f"Game {match_number} of tournament {tournament_name}: win with {desi_team_points - enemy_team_points} points.")
            win_count += 1

        elif enemy_team_points > desi_team_points:
            print(f"Game {match_number} of tournament {tournament_name}: lost with {enemy_team_points - desi_team_points} points.")
            lose_count += 1

        total_matches += 1

win_percentage = (win_count / total_matches) * 100
lose_percentage = (lose_count / total_matches) * 100

print(f"{win_percentage:.2f}% matches win")
print(f"{lose_percentage:.2f}% matches lost")

