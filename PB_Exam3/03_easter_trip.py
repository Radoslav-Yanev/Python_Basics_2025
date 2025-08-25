FRANCE_21_23_PRICE = 30
FRANCE_24_27_PRICE = 35
FRANCE_28_31_PRICE = 40

ITALY_21_23_PRICE = 28
ITALY_24_27_PRICE = 32
ITALY_28_31_PRICE = 39

GERMANY_21_23_PRICE = 32
GERMANY_24_27_PRICE = 37
GERMANY_28_31_PRICE = 43

destination = input()
dates = input()
nights = int(input())

total_price = 0

if destination == "France":
    if dates == "21-23":
        total_price = (FRANCE_21_23_PRICE * nights)

    elif dates == "24-27":
        total_price = (FRANCE_24_27_PRICE * nights)

    elif dates == "28-31":
        total_price = (FRANCE_28_31_PRICE * nights)

elif destination == "Italy":
    if dates == "21-23":
        total_price = (ITALY_21_23_PRICE * nights)

    elif dates == "24-27":
        total_price = (ITALY_24_27_PRICE * nights)

    elif dates == "28-31":
        total_price = (ITALY_28_31_PRICE * nights)

elif destination == "Germany":
    if dates == "21-23":
        total_price = (GERMANY_21_23_PRICE * nights)

    elif dates == "24-27":
        total_price = (GERMANY_24_27_PRICE * nights)

    elif dates == "28-31":
        total_price = (GERMANY_28_31_PRICE * nights)

print(f"Easter trip to {destination} : {total_price:.2f} leva.")

