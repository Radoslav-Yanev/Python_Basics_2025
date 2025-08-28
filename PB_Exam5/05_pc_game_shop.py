bought_games_count = int(input())

sales = {
    "Hearthstone": 0,
    "Fornite": 0,
    "Overwatch": 0,
}

other_games_count = 0

for _ in range(bought_games_count):
    game_name = input()

    if game_name in sales:
        sales[game_name] += 1

    else:
        other_games_count += 1

hearthstone_sales_percentage = (sales["Hearthstone"] / bought_games_count) * 100
fortnite_sales_percentage = (sales["Fornite"] / bought_games_count) * 100
overwatch_sales_percentage = (sales["Overwatch"] / bought_games_count) * 100
others_sales_percentage = (other_games_count / bought_games_count) * 100

print(f"Hearthstone - {hearthstone_sales_percentage:.2f}%\nFornite - {fortnite_sales_percentage:.2f}%"
      f"\nOverwatch - {overwatch_sales_percentage:.2f}%\nOthers - {others_sales_percentage:.2f}%")
