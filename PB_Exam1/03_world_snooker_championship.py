DISCOUNT_ABOVE_4000_LYRES = 0.25
DISCOUNT_ABOVE_2500_LYRES = 0.10
TROPHY_PIC_PRICE = 40

championship_state = input()
ticket_type = input()
ticket_count = int(input())
trophy_pic = input()

ticket_price = 0

if championship_state == "Quarter final":

    if ticket_type == "Standard":
        ticket_price += 55.50

    elif ticket_type == "Premium":
        ticket_price += 105.20

    elif ticket_type == "VIP":
        ticket_price += 118.90


elif championship_state == "Semi final":

    if ticket_type == "Standard":
        ticket_price += 75.88

    elif ticket_type == "Premium":
        ticket_price += 125.22

    elif ticket_type == "VIP":
        ticket_price += 300.40

elif championship_state == "Final":

    if ticket_type == "Standard":
        ticket_price += 110.10

    elif ticket_type == "Premium":
        ticket_price += 160.66

    elif ticket_type == "VIP":
        ticket_price += 400

total_price = ticket_price * ticket_count

if total_price > 4000:
    total_price -= total_price * DISCOUNT_ABOVE_4000_LYRES

elif total_price > 2500:
    total_price -= total_price * DISCOUNT_ABOVE_2500_LYRES

    if trophy_pic == "Y":
        total_price += TROPHY_PIC_PRICE * ticket_count

else:

    if trophy_pic == "Y":
        total_price += TROPHY_PIC_PRICE * ticket_count


print(f"{total_price:.2f}")