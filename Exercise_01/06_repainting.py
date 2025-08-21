NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5.00
PACAGE_PRICE = 0.40

nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
time = int(input())

nylon_needed += 2
paint_needed += (paint_needed * 0.10)

amount = ((nylon_needed * NYLON_PRICE) + (paint_needed * PAINT_PRICE)
          + (thinner_needed * THINNER_PRICE) + PACAGE_PRICE)

worker_price = (amount * 0.30) * time

total_sum = amount + worker_price

print(total_sum)



