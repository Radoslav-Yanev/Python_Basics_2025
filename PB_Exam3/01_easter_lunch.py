EASTER_BREAD_PRICE = 3.20
PRICE_FOR_12EGGS = 4.35
COOKIES_PRICE = 5.40
PAINT_PER_EGGS_PRICE = 0.15

easter_bread_count = int(input())
egg_shells_count = int(input())
kg_cookies = int(input())

easter_bread_sum = easter_bread_count * EASTER_BREAD_PRICE
eggs_price = egg_shells_count * PRICE_FOR_12EGGS
cookies_price = kg_cookies * COOKIES_PRICE
paint_price = (PAINT_PER_EGGS_PRICE * 12) * egg_shells_count

total_price = easter_bread_sum + eggs_price + cookies_price + paint_price

print(f"{total_price:.2f}")