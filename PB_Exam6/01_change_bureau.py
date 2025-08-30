bitcoins = int(input())
yuan = float(input())
commission = float(input())

leva_from_btc = bitcoins * 1168
usd = yuan * 0.15
leva_from_usd = usd * 1.76
total_leva = leva_from_btc + leva_from_usd
euros = total_leva / 1.95
euros_after_commission = euros * (1 - commission / 100)

print(f"{euros_after_commission:.2f}")
