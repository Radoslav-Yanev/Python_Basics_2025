DECOR_PERCENT = 0.10
MORE_THAN_150STATISTS_DISCOUNT = 0.10

discount = 0

film_budget = float(input())
statists_count = int(input())
clothes_price_per_statist = float(input())

decor_price = film_budget * DECOR_PERCENT
statists_clothes_price = statists_count * clothes_price_per_statist

if statists_count > 150:
    discount += statists_clothes_price * MORE_THAN_150STATISTS_DISCOUNT

total_sum = decor_price + statists_clothes_price - discount

if total_sum > film_budget:
    print(f"Not enough money!\nWingard needs {total_sum - film_budget:.2f} leva more.")

else:
    print(f"Action!\nWingard starts filming with {film_budget - total_sum:.2f} leva left.")