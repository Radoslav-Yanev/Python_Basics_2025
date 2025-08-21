film_budget = float(input())
statists_count = int(input())
price_for_clothes_per_statist = float(input())

decor_price = film_budget * 0.10
total_clothes_price = statists_count * price_for_clothes_per_statist

if statists_count > 150:
    total_clothes_price -= total_clothes_price * 0.10

total_price = total_clothes_price + decor_price

if total_price > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {total_price - film_budget:.2f} leva more.")
elif total_price <= film_budget:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - total_price:.2f} leva left.")