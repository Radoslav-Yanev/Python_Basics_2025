budget = float(input())

remaining_budget = budget

while remaining_budget > 0:
    actor_name = input()

    if actor_name == "ACTION":
        break

    if len(actor_name) <= 15:
        reward = float(input())
        money = reward

    else:
        money = remaining_budget * 0.20

    remaining_budget -= money

if remaining_budget >= 0:
    print(f"We are left with {remaining_budget:.2f} leva.")

else:
    print(f"We need {abs(remaining_budget):.2f} leva for our actors.")