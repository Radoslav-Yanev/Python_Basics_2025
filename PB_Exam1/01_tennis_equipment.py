from math import floor, ceil

tennis_racket_price = float(input())
tennis_racket_count = int(input())
sneakers_count = int(input())

other_equipment = 0

sneakers_price = tennis_racket_price / 6
equipments_sum = (tennis_racket_price * tennis_racket_count) + (sneakers_price * sneakers_count)
other_equipment += equipments_sum * 0.20

total_sum = equipments_sum + other_equipment

johovich_share = total_sum / 8
sponsor_share = total_sum * 7/8

print(f"Price to be paid by Djokovic {floor(johovich_share)}")
print(f"Price to be paid by sponsors {ceil(sponsor_share)}")