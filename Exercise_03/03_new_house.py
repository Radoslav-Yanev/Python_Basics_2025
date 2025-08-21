ROSE_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

ROSE_DISCOUNT = 0.10
DAHLIAS_DISCOUNT = 0.15
TULIPS_DISCOUNT = 0.15
NARCISSUS_INCREASE = 0.15
GLADIOLUS_INCREASE = 0.20

flower_type = (input())
flower_count = int(input())
budged = int(input())

total_price = 0

if flower_type == "Roses":
    total_price = flower_count * ROSE_PRICE

    if flower_count > 80:
        total_price -= total_price * ROSE_DISCOUNT

elif flower_type == "Dahlias":
    total_price = flower_count * DAHLIAS_PRICE

    if flower_count > 90:
        total_price -= total_price * DAHLIAS_DISCOUNT

elif flower_type == "Tulips":
    total_price = flower_count * TULIPS_PRICE

    if flower_count > 80:
        total_price -= total_price * TULIPS_DISCOUNT

elif flower_type == "Narcissus":
    total_price = flower_count * NARCISSUS_PRICE

    if flower_count < 120:
        total_price += total_price * NARCISSUS_INCREASE

elif flower_type == "Gladiolus":
    total_price = flower_count * GLADIOLUS_PRICE

    if flower_count < 80:
        total_price += total_price * GLADIOLUS_INCREASE


if budged >= total_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budged - total_price:.2f} leva left.")
elif budged < total_price:
    print(f"Not enough money, you need {total_price - budged:.2f} leva more.")