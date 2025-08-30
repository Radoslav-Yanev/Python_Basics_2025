dog_food_quantity = int(input()) * 1000

total_eaten_food = 0

while True:
    command = input()

    if command == "Adopted":
        break

    eaten_food_in_gr = int(command)

    total_eaten_food += eaten_food_in_gr

if dog_food_quantity >= total_eaten_food:
    print(f"Food is enough! Leftovers: {dog_food_quantity - total_eaten_food} grams." )

else:
    print(f"Food is not enough. You need {abs(dog_food_quantity - total_eaten_food)} grams more.")


