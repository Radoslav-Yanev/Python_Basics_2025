day_count = int(input())

total_wins = 0
total_loses = 0
total_money = 0

for _ in range(day_count):
    wins = 0
    loses = 0
    day_money = 0

    while True:
        sport = input()

        if sport == "Finish":
            break

        result = input()

        if result == "win":
            day_money += 20
            wins += 1

        elif result == "lose":
            loses += 1

    if wins > loses:
        day_money *= 1.10
        total_wins += 1

    elif loses > wins:
        total_loses += 1

    total_money += day_money

if total_wins > total_loses:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")

elif total_wins < total_loses:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")

