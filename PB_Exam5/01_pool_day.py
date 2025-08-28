from math import ceil

peoples_count = int(input())
tax = float(input())
price_per_deckchair = float(input())
price_per_umbrella = float(input())

total_tax = tax * peoples_count
total_umbrella_price = price_per_umbrella * ceil(peoples_count / 2)
deckchair_total_price = price_per_deckchair * ceil(peoples_count * 0.75)

total_price = total_tax + total_umbrella_price + deckchair_total_price

print(f"{total_price:.2f} lv." )
