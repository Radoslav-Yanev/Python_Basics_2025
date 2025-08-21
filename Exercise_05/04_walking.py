GOAL_STEPS = 10_000

total_steps = 0

while total_steps < GOAL_STEPS:
    current_steps = input()

    if current_steps == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        break

    total_steps += int(current_steps)

if total_steps >= GOAL_STEPS:
    print(f"Goal reached! Good job!\n{total_steps - GOAL_STEPS} steps over the goal!")

else:
    print(f"{GOAL_STEPS - total_steps} more steps to reach goal.")