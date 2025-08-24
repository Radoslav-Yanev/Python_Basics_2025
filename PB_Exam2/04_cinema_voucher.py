voucher_value = int(input())
purchase_ticket_count = 0
purchase_other_thinks_count = 0

while True:
    purchase = input()

    if purchase == "End":
        break

    price = 0

    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price > voucher_value:
            break

        purchase_ticket_count += 1

    else:
        price = ord(purchase[0])
        if price > voucher_value:
            break

        purchase_other_thinks_count += 1

    voucher_value -= price

print(f"{purchase_ticket_count}")
print(f"{purchase_other_thinks_count}")


