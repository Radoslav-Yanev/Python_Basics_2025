FROM_400_TO_1000LV_DISCOUNT_PER = 0.85
ABOVE_1000LV = 0.50

fruit = input()
set_size = input()
sets_count = int(input())

price = {
    "Watermelon": {
        "small": 56,
        "big": 28.70
    },
    "Mango": {
        "small": 36.66,
        "big": 19.60
    },
    "Pineapple": {
        "small": 42.10,
        "big": 24.80
    },
    "Raspberry": {
        "small": 20,
        "big": 15.20
    },
}

amount = price[fruit][set_size] * sets_count

if set_size == "big":
    amount *= 5
elif set_size == "small":
    amount *= 2

if 400 <= amount <= 1000:
    amount *= FROM_400_TO_1000LV_DISCOUNT_PER

elif amount > 1000:
    amount *= ABOVE_1000LV

print(f"{amount:.2f} lv.")