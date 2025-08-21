LILY_BROTHER_TAXES_PRICE = 1

lily_age = int(input())
washing_machine_price = float(input())
unit_toy_price = int(input())

increase_money = 10
toy_count = 0
total_money = 0

for age in range(1, lily_age + 1):

    if age % 2 == 0:
        total_money += (increase_money - LILY_BROTHER_TAXES_PRICE)

        increase_money += 10

    else:
        toy_count += 1


total_toy_price = toy_count * unit_toy_price

total_money += total_toy_price

if total_money >= washing_machine_price:
    print(f"Yes! {total_money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total_money:.2f}")