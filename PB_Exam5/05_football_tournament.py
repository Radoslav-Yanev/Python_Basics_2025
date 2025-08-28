team_name = input()
match_count = int(input())

score = {"W": 0, "D": 0, "L": 0}
points = 0

for _ in range(match_count):
    current_result = input()

    if current_result in score:
        score[current_result] += 1
        if current_result == "W":
            points += 3
        elif current_result == "D":
            points += 1

if match_count == 0:
    print(f"{team_name} hasn't played any games during this season.")

else:
    win_rate_percentage = (score["W"] / match_count) * 100
    print(f"{team_name} has won {points} points during this season.\nTotal stats:"
          f"\n## W: {score['W']}"
          f"\n## D: {score['D']}"
          f"\n## L: {score['L']}"
          f"\nWin rate: {win_rate_percentage:.2f}%")
