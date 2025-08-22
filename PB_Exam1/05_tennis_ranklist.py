from math import floor

W_POINTS = 2000
F_POINTS = 1200
SF_POINTS = 720

tournaments_count = int(input())
start_points = int(input())

points = 0
tournaments_win_count = 0

for _ in range(tournaments_count):
    stage = input()

    if stage == "W":
        points += W_POINTS
        tournaments_win_count += 1

    elif stage == "F":
        points += F_POINTS

    elif stage == "SF":
        points += SF_POINTS

total_points = points + start_points
average_points = points / tournaments_count
win_tournaments_percentage = (tournaments_win_count / tournaments_count) * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{win_tournaments_percentage:.2f}%")