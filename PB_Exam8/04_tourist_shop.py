budget = float(input())

sold_product_count = 0
total_price = 0

while True:
    product_name = input()

    if product_name == "Stop":
        print(f"You bought {sold_product_count} products for {total_price:.2f} leva.")
        break

    product_price = float(input())
    sold_product_count += 1

    if sold_product_count % 3 == 0:
        product_price /= 2

    if product_price > budget:
        print(f"You don't have enough money!\nYou need {abs(budget - product_price):.2f} leva!")
        break

    total_price += product_price
    budget -= product_price




