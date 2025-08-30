budget = float(input())
fuel_in_lt = float(input())
day_of_week = input()

fuel_price_per_lt = 2.10
guide_price = 100

discount = {
    "Saturday": 0.90,
    "Sunday": 0.80
}

price = ((fuel_in_lt * fuel_price_per_lt) + guide_price)
total_price = price * discount[day_of_week]

if total_price > budget:
    print(f"Not enough money! Money needed: {total_price - budget:.2f} lv.")

else:
    print(f"Safari time! Money left: {abs(total_price - budget):.2f} lv. ")