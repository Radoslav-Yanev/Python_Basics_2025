UNDER_19Y_DISCOUNT = 0.80

budget = float(input())
gender = input()
age = int(input())
sport = input()

price = {
    "Gym": {"m": 42, "f": 35},
    "Boxing": {"m": 41, "f": 37},
    "Yoga": {"m": 45, "f": 42},
    "Zumba": {"m": 34, "f": 31},
    "Dances": {"m": 51, "f": 53},
    "Pilates": {"m": 39, "f": 37},
}

amount = price[sport][gender]

if age <= 19:
    amount *= UNDER_19Y_DISCOUNT

if budget >= amount:
    print(f"You purchased a 1 month pass for {sport}.")

else:
    print(f"You don't have enough money! You need ${abs(budget - amount):.2f} more.")