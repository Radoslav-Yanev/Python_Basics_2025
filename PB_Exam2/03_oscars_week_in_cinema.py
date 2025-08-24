STAR_IS_BORN_NORMAL_PRICE = 7.50
STAR_IS_BORN_LUXURY_PRICE = 10.50
STAR_IS_BORN_ULTRA_LUXURY_PRICE = 13.50

BOHEMIAN_RHAPSODY_NORMAL_PRICE = 7.35
BOHEMIAN_RHAPSODY_LUXURY_PRICE = 9.45
BOHEMIAN_RHAPSODY_ULTRA_LUXURY_PRICE = 12.75

GREEN_BOOK_NORMAL_PRICE = 8.15
GREEN_BOOK_LUXURY_PRICE = 10.25
GREEN_BOOK_ULTRA_LUXURY_PRICE = 13.25

THE_FAVOURITE_NORMAL_PRICE = 8.75
THE_FAVOURITE_LUXURY_PRICE = 11.55
THE_FAVOURITE_ULTRA_LUXURY_PRICE = 13.95

film_name = input()
hall_type = input()
ticket_count = int(input())

price = 0

if hall_type == "normal":

    if film_name == "A Star Is Born":
        price += ticket_count * STAR_IS_BORN_NORMAL_PRICE

    elif film_name == "Bohemian Rhapsody":
        price += ticket_count * BOHEMIAN_RHAPSODY_NORMAL_PRICE

    elif film_name == "Green Book":
        price += ticket_count * GREEN_BOOK_NORMAL_PRICE

    elif film_name == "The Favourite":
        price += ticket_count * THE_FAVOURITE_NORMAL_PRICE


elif hall_type == "luxury":

    if film_name == "A Star Is Born":
        price += ticket_count * STAR_IS_BORN_LUXURY_PRICE

    elif film_name == "Bohemian Rhapsody":
        price += ticket_count * BOHEMIAN_RHAPSODY_LUXURY_PRICE

    elif film_name == "Green Book":
        price += ticket_count * GREEN_BOOK_LUXURY_PRICE

    elif film_name == "The Favourite":
        price += ticket_count * THE_FAVOURITE_LUXURY_PRICE

elif hall_type == "ultra luxury":

    if film_name == "A Star Is Born":
        price += ticket_count * STAR_IS_BORN_ULTRA_LUXURY_PRICE

    elif film_name == "Bohemian Rhapsody":
        price += ticket_count * BOHEMIAN_RHAPSODY_ULTRA_LUXURY_PRICE

    elif film_name == "Green Book":
        price += ticket_count * GREEN_BOOK_ULTRA_LUXURY_PRICE

    elif film_name == "The Favourite":
        price += ticket_count * THE_FAVOURITE_ULTRA_LUXURY_PRICE

print(f"{film_name} -> {price:.2f} lv.")