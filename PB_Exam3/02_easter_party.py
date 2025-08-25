DISCOUNT_BETWEEN_10_15_PERSONS = 0.15
DISCOUNT_BETWEEN_15_20_PERSONS = 0.20
DISCOUNT_ABOVE_20_PERSONS = 0.25

CAKE_PRICE_PERCENTAGE = 0.10

guests_count = int(input())
cover_price_per_person = float(input())
desi_budget = float(input())

cake_price = desi_budget * CAKE_PRICE_PERCENTAGE

if 10 <= guests_count <= 15:
    cover_price_per_person -= cover_price_per_person * DISCOUNT_BETWEEN_10_15_PERSONS

elif 15 <= guests_count <= 20:
    cover_price_per_person -= cover_price_per_person * DISCOUNT_BETWEEN_15_20_PERSONS

elif guests_count > 20:
    cover_price_per_person -= cover_price_per_person * DISCOUNT_ABOVE_20_PERSONS

total_sum = (guests_count * cover_price_per_person) + cake_price

if desi_budget >= total_sum:
    print(f"It is party time! {desi_budget - total_sum:.2f} leva left.")

else:
    print(f"No party! {total_sum - desi_budget:.2f} leva needed.")