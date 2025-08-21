BULGARIA_BUDGET_LIMIT = 100
BALKANS_BUDGET_LIMIT = 1000

BULGARIA_SUMMER_DISCOUNT = 0.30
BULGARIA_WINTER_DISCOUNT = 0.70
BALKANS_SUMMER_DISCOUNT = 0.40
BALKANS_WINTER_DISCOUNT = 0.80
EUROPE_JOURNEY_DISCOUNT = 0.90

budget = float(input())
season = input()

destination = ""
type_of_vacation = ""
spend_sum = 0

if season == "summer":

    if budget <= BULGARIA_BUDGET_LIMIT:
        spend_sum = budget * BULGARIA_SUMMER_DISCOUNT
        type_of_vacation = "Camp"
        destination = "Bulgaria"
    elif BULGARIA_BUDGET_LIMIT < budget <= BALKANS_BUDGET_LIMIT:
        spend_sum = budget * BALKANS_SUMMER_DISCOUNT
        type_of_vacation = "Camp"
        destination = "Balkans"
    else:
        spend_sum = budget * EUROPE_JOURNEY_DISCOUNT
        type_of_vacation = "Hotel"
        destination = "Europe"

elif season == "winter":

    if budget <= BULGARIA_BUDGET_LIMIT:
        spend_sum = budget * BULGARIA_WINTER_DISCOUNT
        type_of_vacation = "Hotel"
        destination = "Bulgaria"
    elif BULGARIA_BUDGET_LIMIT < budget <= BALKANS_BUDGET_LIMIT:
        spend_sum = budget * BALKANS_WINTER_DISCOUNT
        type_of_vacation = "Hotel"
        destination = "Balkans"
    else:
        spend_sum = budget * EUROPE_JOURNEY_DISCOUNT
        type_of_vacation = "Hotel"
        destination = "Europe"


print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {spend_sum:.2f}")