fitness_clients = int(input())

back_total_peoples = 0
chest_total_peoples = 0
legs_total_peoples = 0
abs_total_peoples = 0
protein_shake_buyers = 0
protein_bar_buyers = 0

for _ in range(fitness_clients):
    activity = input()

    if activity == "Back":
        back_total_peoples += 1

    elif activity == "Chest":
        chest_total_peoples += 1

    elif activity == "Legs":
        legs_total_peoples += 1

    elif activity == "Abs":
        abs_total_peoples += 1

    elif activity == "Protein shake":
        protein_shake_buyers += 1

    elif activity == "Protein bar":
        protein_bar_buyers += 1

training_peoples_percentage = ((back_total_peoples + chest_total_peoples + legs_total_peoples + abs_total_peoples) / fitness_clients ) * 100
protein_buyers_percentage = ((protein_shake_buyers + protein_bar_buyers) / fitness_clients) * 100

print(f"{back_total_peoples} - back")
print(f"{chest_total_peoples} - chest")
print(f"{legs_total_peoples} - legs")
print(f"{abs_total_peoples} - abs")
print(f"{protein_shake_buyers} - protein shake")
print(f"{protein_bar_buyers} - protein bar")
print(f"{training_peoples_percentage:.2f}% - work out")
print(f"{protein_buyers_percentage:.2f}% - protein")