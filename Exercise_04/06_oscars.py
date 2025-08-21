MIN_POINTS = 1250.5

actor_name = input()
academy_points = float(input())
evaluators_count = int(input())

is_nominate = False

for _ in range(evaluators_count):
    evaluator_name = input()
    evaluator_points = float(input())

    academy_points += (len(evaluator_name) * evaluator_points / 2)

    if academy_points > MIN_POINTS:
        is_nominate = True
        break

if is_nominate:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")

else:
    print(f"Sorry, {actor_name} you need {MIN_POINTS - academy_points:.1f} more!")