SHIP_SPRING_PRICE = 3000
SHIP_SUMMER_AUTUMN_PRICE = 4200
SHIP_WINTER_PRICE = 2600

SMALL_GROUP_DISCOUNT = 0.10
MEDIUM_GROUP_DISCOUNT = 0.15
LARGE_GROUP_DISCOUNT = 0.25
EVEN_FISHERMEN_DISCOUNT = 0.05

group_budget = int(input())
season = input()
fishermen_count = int(input())

price_for_rent = 0

if season == "Spring":
    price_for_rent = SHIP_SPRING_PRICE

elif season == "Summer" or season == "Autumn":
    price_for_rent = SHIP_SUMMER_AUTUMN_PRICE

elif season == "Winter":
    price_for_rent = SHIP_WINTER_PRICE

if 1 <= fishermen_count <= 6:
    price_for_rent -= (price_for_rent * SMALL_GROUP_DISCOUNT)

elif 7 <= fishermen_count <= 11:
    price_for_rent -= (price_for_rent * MEDIUM_GROUP_DISCOUNT)

elif fishermen_count >= 12:
    price_for_rent -= (price_for_rent * LARGE_GROUP_DISCOUNT)

if fishermen_count % 2 == 0 and season != "Autumn":
    price_for_rent -= (price_for_rent * EVEN_FISHERMEN_DISCOUNT)

if price_for_rent <= group_budget:
    print(f"Yes! You have {group_budget - price_for_rent:.2f} leva left.")
else:
    print(f"Not enough money! You need {price_for_rent - group_budget:.2f} leva.")


# SECOND WAY

# SHIP_SPRING_PRICE = 3000
# SHIP_SUMMER_AUTUMN_PRICE = 4200
# SHIP_WINTER_PRICE = 2600
#
# SMALL_GROUP_DISCOUNT = 0.10
# MEDIUM_GROUP_DISCOUNT = 0.15
# LARGE_GROUP_DISCOUNT = 0.25
# EVEN_FISHERMEN_DISCOUNT = 0.05
#
# group_budget = int(input())
# season = input()
# fishermen_count = int(input())
#
# price_for_rent = 0
#
# if season == "Spring":
#  price_for_rent = SHIP_SPRING_PRICE
#
#  if 1 <= fishermen_count <= 6:
#      price_for_rent -= (price_for_rent * SMALL_GROUP_DISCOUNT)
#
#  elif 7 <= fishermen_count <= 11:
#      price_for_rent -= (price_for_rent * MEDIUM_GROUP_DISCOUNT)
#
#  elif fishermen_count >= 12:
#      price_for_rent -= (price_for_rent * LARGE_GROUP_DISCOUNT)
#
# elif season == "Summer" or season == "Autumn":
#         price_for_rent = SHIP_SUMMER_AUTUMN_PRICE
#
#         if 1 <= fishermen_count <= 6:
#             price_for_rent -= (price_for_rent * SMALL_GROUP_DISCOUNT)
#
#         elif 7 <= fishermen_count <= 11:
#             price_for_rent -= (price_for_rent * MEDIUM_GROUP_DISCOUNT)
#
#         elif fishermen_count >= 12:
#             price_for_rent -= (price_for_rent * LARGE_GROUP_DISCOUNT)
#
# elif season == "Winter":
#     price_for_rent = SHIP_WINTER_PRICE
#
#     if 1 <= fishermen_count <= 6:
#         price_for_rent -= (price_for_rent * SMALL_GROUP_DISCOUNT)
#
#     elif 7 <= fishermen_count <= 11:
#         price_for_rent -= (price_for_rent * MEDIUM_GROUP_DISCOUNT)
#
#     elif fishermen_count >= 12:
#         price_for_rent -= (price_for_rent * LARGE_GROUP_DISCOUNT)
#
# if fishermen_count % 2 == 0 and season != "Autumn":
#     price_for_rent -= (price_for_rent * EVEN_FISHERMEN_DISCOUNT)
#
# if price_for_rent <= group_budget:
#     print(f"Yes! You have {group_budget - price_for_rent:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {price_for_rent - group_budget:.2f} leva.")