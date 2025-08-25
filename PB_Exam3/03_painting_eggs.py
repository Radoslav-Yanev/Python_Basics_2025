LARGE_RED_EGG_PRICE = 16
LARGE_GREEN_EGG_PRICE = 12
LARGE_YELLOW_EGG_PRICE = 9

MEDIUM_RED_EGG_PRICE = 13
MEDIUM_GREEN_EGG_PRICE = 9
MEDIUM_YELLOW_EGG_PRICE = 7

SMALL_RED_EGG_PRICE = 9
SMALL_GREEN_EGG_PRICE = 8
SMALL_YELLOW_EGG_PRICE = 5

PRODUCTION_COST_PERCENTAGE = 0.35

eggs_size = input()
eggs_color = input()
batch_count = int(input())

total_cost = 0

if eggs_size == "Large":
    if eggs_color == "Red":
        total_cost = (LARGE_RED_EGG_PRICE * batch_count)

    elif eggs_color == "Green":
        total_cost = (LARGE_GREEN_EGG_PRICE * batch_count)

    elif eggs_color == "Yellow":
        total_cost = (LARGE_YELLOW_EGG_PRICE * batch_count)

elif eggs_size == "Medium":
    if eggs_color == "Red":
        total_cost = (MEDIUM_RED_EGG_PRICE * batch_count)

    elif eggs_color == "Green":
        total_cost = (MEDIUM_GREEN_EGG_PRICE * batch_count)

    elif eggs_color == "Yellow":
        total_cost = (MEDIUM_YELLOW_EGG_PRICE * batch_count)

elif eggs_size == "Small":
    if eggs_color == "Red":
        total_cost = (SMALL_RED_EGG_PRICE * batch_count)

    elif eggs_color == "Green":
        total_cost = (SMALL_GREEN_EGG_PRICE * batch_count)

    elif eggs_color == "Yellow":
        total_cost = (SMALL_YELLOW_EGG_PRICE * batch_count)

production_cost = total_cost * PRODUCTION_COST_PERCENTAGE
total_cost -= production_cost

print(f"{total_cost:.2f} leva.")