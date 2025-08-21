SUDIO_MAY_OCTOBER_PRICE_PER_NIGHT = 50
SUDIO_JUNE_SEPTEMBER_PRICE_PER_NIGHT = 75.20
SUDIO_JULY_AUGUST_PRICE_PER_NIGHT = 76

APARTMENT_MAY_OCTOBER_PRICE_PER_NIGHT = 65
APARTMENT_JUNE_SEPTEMBER_PRICE_PER_NIGHT = 68.70
APARTMENT_JULY_AUGUST_PRICE_PER_NIGHT = 77

STUDIO_MAY_OCTOBER_DISC_7NIGHTS = 0.05
STUDIO_MAY_OCTOBER_DISC_14NIGHTS = 0.30
STUDIO_JUNE_SEPTEMBER_DISC_14NIGHTS = 0.20
APARTMENT_DISC_14NIGHTS = 0.10

month = input()
night_count = int(input())

apartment_sum = 0
studio_sum = 0

if month == "May" or month == "October":
    studio_sum = SUDIO_MAY_OCTOBER_PRICE_PER_NIGHT * night_count
    apartment_sum = APARTMENT_MAY_OCTOBER_PRICE_PER_NIGHT * night_count

    if night_count > 14:
        studio_sum -= studio_sum * STUDIO_MAY_OCTOBER_DISC_14NIGHTS
    elif night_count > 7:
        studio_sum -= studio_sum * STUDIO_MAY_OCTOBER_DISC_7NIGHTS

elif month == "June" or month == "September":
    studio_sum = SUDIO_JUNE_SEPTEMBER_PRICE_PER_NIGHT * night_count
    apartment_sum = APARTMENT_JUNE_SEPTEMBER_PRICE_PER_NIGHT * night_count

    if night_count > 14:
        studio_sum -= studio_sum * STUDIO_JUNE_SEPTEMBER_DISC_14NIGHTS

elif month == "July" or month == "August":
    studio_sum = SUDIO_JULY_AUGUST_PRICE_PER_NIGHT * night_count
    apartment_sum = APARTMENT_JULY_AUGUST_PRICE_PER_NIGHT * night_count

if night_count > 14:
    apartment_sum -= apartment_sum * APARTMENT_DISC_14NIGHTS

print(f"Apartment: {apartment_sum:.2f} lv.")
print(f"Studio: {studio_sum:.2f} lv.")