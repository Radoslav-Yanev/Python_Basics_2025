TICKET_PRICE = 5
DISCOUNT = 5

hall_capacity = int(input())

total_money = 0
occupied_seats = 0

while True:
    command = input()

    if command == "Movie time!":
        print(f"There are {hall_capacity - occupied_seats} seats left in the cinema.")
        break

    peoples = int(command)

    if peoples > hall_capacity - occupied_seats:
        print(f"The cinema is full.")
        break

    occupied_seats += peoples
    total_money += peoples * TICKET_PRICE - (DISCOUNT if peoples % 3 == 0 else 0)

print(f"Cinema income - {total_money} lv.")