target_profit = float(input())

total_profit = 0

while True:
    cocktail_name = input()

    if cocktail_name == "Party!":
        if total_profit >= target_profit:
            print("Target acquired.")
        else:
            print(f"We need {(target_profit - total_profit):.2f} leva more.")
        break

    cocktail_count = int(input())

    price = len(cocktail_name) * cocktail_count

    if price % 2 != 0:
        price *= 0.75

    total_profit += price

    if total_profit >= target_profit:
        print("Target acquired.")
        break

print(f"Club income - {total_profit:.2f} leva.")

