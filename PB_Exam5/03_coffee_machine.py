price = {
    "Espresso": {
       "Without": 0.90,
       "Normal": 1.00,
       "Extra": 1.20
    },
    "Cappuccino": {
        "Without": 1.00,
        "Normal": 1.20,
        "Extra": 1.60
    },
    "Tea": {
        "Without": 0.50,
        "Normal": 0.60,
        "Extra": 0.70
    }
}

drink_type = input()
sugar_type = input()
drink_count = int(input())

total_price = 0

if drink_type in price:
    if sugar_type in price[drink_type]:
        total_price = price[drink_type][sugar_type] * drink_count

if sugar_type == "Without":
    total_price *= 0.65

if drink_type == "Espresso" and drink_count >= 5:
    total_price *= 0.75

if total_price > 15:
    total_price *= 0.80


print(f"You bought {drink_count} cups of {drink_type} for {total_price:.2f} lv.")


