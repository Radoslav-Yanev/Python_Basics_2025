from math import floor

tournaments_count = int(input())
starting_point = int(input())

earned_points = 0
wins = 0

for _ in range(tournaments_count):
    current_tournament_state = input()

    if current_tournament_state == "W":
        earned_points += 2000
        wins += 1
    elif current_tournament_state == "F":
        earned_points += 1200
    elif current_tournament_state == "SF":
        earned_points += 720

total_point = starting_point + earned_points

average_point = earned_points / tournaments_count

wins_percentage = (wins / tournaments_count) * 100

print(f"Final points: {total_point}")
print(f"Average points: {floor(average_point)}")
print(f"{wins_percentage:.2f}%")