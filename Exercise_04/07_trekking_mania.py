group_count = int(input())

count_musala = 0
count_monblan = 0
count_kilimanjaro = 0
count_k2 = 0
count_everest = 0


for _ in range(group_count):
    people_count = int(input())

    if  people_count <= 5:
        count_musala += people_count

    elif 6 <= people_count <= 12:
        count_monblan += people_count

    elif 13 <= people_count <= 25:
        count_kilimanjaro += people_count

    elif 26 <= people_count <= 40:
        count_k2 += people_count

    elif people_count >= 41:
        count_everest += people_count

total_count = count_musala + count_monblan + count_kilimanjaro + count_k2 + count_everest

musala_percent = count_musala / total_count * 100
monblan_percent = count_monblan / total_count * 100
kilimanjaro_percent = count_kilimanjaro / total_count * 100
k2_percent = count_k2 / total_count * 100
everest_percent = count_everest / total_count * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")