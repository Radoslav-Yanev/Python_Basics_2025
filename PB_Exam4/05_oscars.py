max_points = 1250.5

actor_name = input()
academy_points = float(input())
evaluators_count = int(input())

is_goal_achieved = False

for _ in range(evaluators_count):
    evaluator_name = input()
    current_points = float(input())

    academy_points += (len(evaluator_name) * current_points) / 2

    if academy_points > max_points:
        is_goal_achieved = True
        break

if is_goal_achieved:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")

else: print(f"Sorry, {actor_name} you need {abs(academy_points - max_points):.1f} more!")
