discount = {
"Thrones": 0.50,
"Lucifer": 0.60,
"Protector": 0.70,
"TotalDrama": 0.80,
"Area": 0.90
}

budget = float(input())
series_count = int(input())

total_price = 0

for _ in range(series_count):
    series_name = input()
    price = float(input())

    if series_name in discount:
        price *= discount[series_name]

    total_price += price

if budget >= total_price:
    print(f"You bought all the series and left with {budget - total_price:.2f} lv.")

else:
    print(f"You need {abs(budget - total_price):.2f} lv. more to buy the series!")