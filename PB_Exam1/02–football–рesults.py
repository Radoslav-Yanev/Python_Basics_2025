first_match_score = input()
second_match_score = input()
third_match_score = input()

wins = 0
draws = 0
loses = 0

matches = [first_match_score, second_match_score, third_match_score]

for match in matches:
    team_goals, opponents_goals = match.split(':')
    team_points = int(team_goals)
    opponents_points = int(opponents_goals)

    if team_points > opponents_points:
        wins += 1

    elif team_points == opponents_points:
        draws += 1

    elif team_points < opponents_points:
        loses += 1


print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f" Drawn games: {draws}")