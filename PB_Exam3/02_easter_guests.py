from math import ceil

EASTER_BREAD_PRICE = 4
ONE_EGG_PRICE = 0.45

guests_count = int(input())
budget = int(input())

easter_bread_count = ceil(guests_count / 3)
eggs_count = ceil(guests_count * 2)
total_price = (easter_bread_count * EASTER_BREAD_PRICE) + (eggs_count * ONE_EGG_PRICE)

if budget >= total_price:
    print(f"Lyubo bought {easter_bread_count} Easter bread and {eggs_count} eggs.")
    print(f"He has {budget - total_price:.2f} lv. left.")

else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {total_price - budget:.2f} lv. more.")
