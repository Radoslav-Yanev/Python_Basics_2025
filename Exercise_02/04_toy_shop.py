PUZZLE_PRICE = 2.60
DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2
DISCOUNT = 0.25
RENT_PRICE = 0.10

excursion_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

total_toy_count = puzzle_count + doll_count + teddy_bear_count + minion_count + truck_count
total_toy_price = ((puzzle_count * PUZZLE_PRICE)
                   + (doll_count * DOLL_PRICE)
                   + (teddy_bear_count * TEDDY_BEAR_PRICE)
                   + (minion_count * MINION_PRICE)
                   + (truck_count * TRUCK_PRICE))

if total_toy_count >= 50:
    total_toy_price -= (total_toy_price * DISCOUNT)

total_toy_price -= (total_toy_price * RENT_PRICE)

if total_toy_price >= excursion_price:
    print(f"Yes! {total_toy_price - excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {(excursion_price - total_toy_price):.2f} lv needed.")