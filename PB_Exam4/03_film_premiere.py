film_name = input()
film_pacage = input()
ticket_count = int(input())

price = {
    "John Wick": {"Drink": 12, "Popcorn": 15, "Menu": 19},
    "Star Wars": {"Drink": 18, "Popcorn": 25, "Menu": 30},
    "Jumanji": {"Drink": 9, "Popcorn": 11, "Menu": 14}
}

total_money = price[film_name][film_pacage] * ticket_count

if film_name == "Star Wars" and ticket_count >= 4:
    total_money *= 0.70

elif film_name == "Jumanji" and ticket_count == 2:
    total_money *= 0.85

print(f"Your bill is {total_money:.2f} leva.")
