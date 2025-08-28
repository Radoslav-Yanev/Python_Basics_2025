price = {
    "Bansko": {
        "withEquipment": {"price": 100, "vip": 0.90},
        "noEquipment": {"price": 80, "vip": 0.95},
    },
    "Borovets": {
        "withEquipment": {"price": 100, "vip": 0.90},
        "noEquipment": {"price": 80, "vip": 0.95},
    },
    "Varna": {
        "withBreakfast": {"price": 130, "vip": 0.88},
        "noBreakfast": {"price": 100, "vip": 0.93},
    },
    "Burgas": {
        "withBreakfast": {"price": 130, "vip": 0.88},
        "noBreakfast": {"price": 100, "vip": 0.93},
    }
}

city_name = input()
pacage_type = input()
vip = input()
day_count = int(input())

if day_count < 1:
    print("Days must be positive number!")

elif city_name not in price or pacage_type not in price[city_name]:
    print("Invalid input!")

else:

    if day_count > 7:
        day_count -= 1

    base_price = price[city_name][pacage_type]["price"]
    vip_discount = price[city_name][pacage_type]["vip"]

    if vip == "yes":
        base_price *= vip_discount

    total_price = base_price * day_count

    print(f"The price is {total_price:.2f}lv! Have a nice time!")