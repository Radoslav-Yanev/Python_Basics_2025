ROOM_FOR_ONE_PERSON_PRICE = 18
APARTMENT_PRICE = 25
PRESIDENT_APARTMENT_PRICE = 35

APARTMENT_LESS_10DAYS_DISC = 0.30
APARTMENT_BETWEEN_10_15DAYS_DISC = 0.35
APARTMENT_MORE_15DAYS_DISC = 0.50

PRESIDENT_APARTMENT_LESS_10DAYS_DISC = 0.10
PRESIDENT_BETWEEN_10_15DAYS_DISC = 0.15
PRESIDENT_MORE_15DAYS_DISC = 0.20

POSITIVE_EVALUATION_DISC = 0.25
NEGATIVE_EVALUATION_DISC = 0.10


day_count = int(input())
room_type = input()
evaluation = input()

nights = day_count - 1
total_sum = 0

if room_type == "apartment":
    total_sum = nights * APARTMENT_PRICE

    if day_count < 10:
        total_sum -= total_sum * APARTMENT_LESS_10DAYS_DISC
    elif 10 <= day_count <= 15:
        total_sum -= total_sum * APARTMENT_BETWEEN_10_15DAYS_DISC
    elif day_count > 15:
        total_sum -= total_sum * APARTMENT_MORE_15DAYS_DISC

elif room_type == "president apartment":
    total_sum = nights * PRESIDENT_APARTMENT_PRICE

    if day_count < 10:
        total_sum -= total_sum * PRESIDENT_APARTMENT_LESS_10DAYS_DISC
    elif 10 <= day_count <= 15:
        total_sum -= total_sum * PRESIDENT_BETWEEN_10_15DAYS_DISC
    elif day_count > 15:
        total_sum -= total_sum * PRESIDENT_MORE_15DAYS_DISC

elif room_type == "room for one person":
    total_sum = nights * ROOM_FOR_ONE_PERSON_PRICE

if evaluation == "positive":
    total_sum += total_sum * POSITIVE_EVALUATION_DISC
elif evaluation == "negative":
    total_sum -= total_sum * NEGATIVE_EVALUATION_DISC

print(f"{total_sum:.2f}")