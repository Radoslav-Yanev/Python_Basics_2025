groups_count = int(input())

total_peoples = 0
musala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for _ in range(groups_count):
    current_peoples_count = int(input())

    if current_peoples_count <= 5:
        musala_count += current_peoples_count

    elif 6 <= current_peoples_count <= 12:
        monblan_count += current_peoples_count

    elif 13 <= current_peoples_count <= 25:
        kilimanjaro_count += current_peoples_count

    elif 26 <= current_peoples_count <= 40:
        k2_count += current_peoples_count

    else:
        everest_count += current_peoples_count

    total_peoples += current_peoples_count

musala_percentage = (musala_count / total_peoples) * 100
monblan_percentage = (monblan_count / total_peoples) * 100
kilimanjaro_percentage = (kilimanjaro_count / total_peoples) * 100
k2_percentage = (k2_count / total_peoples) * 100
everest_percentage = (everest_count / total_peoples) * 100

print(f"{musala_percentage:.2f}%")
print(f"{monblan_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")

