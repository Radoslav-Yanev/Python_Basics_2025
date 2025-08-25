BASKET_PRICE = 1.50
WREATH_PRICE = 3.80
CHOCOLATE_PRICE = 7.00

clients_count = int(input())
total_price = 0

for _ in range(clients_count):
    price = 0
    purchase_count = 0

    while True:
        purchase = input()

        if purchase == "Finish":
            break

        if purchase == "basket":
            price += BASKET_PRICE

        elif purchase == "wreath":
            price += WREATH_PRICE

        elif purchase == "chocolate bunny":
            price += CHOCOLATE_PRICE

        purchase_count += 1

    if purchase_count % 2 == 0:
        price -= (price * 0.20)

    total_price += price
    print(f"You purchased {purchase_count} items for {price:.2f} leva.")

average_cost = total_price / clients_count
print(f"Average bill per client is: {average_cost:.2f} leva.")



