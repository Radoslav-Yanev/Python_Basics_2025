BONUS_POINTS = 0
starter_points = int(input())

if starter_points <= 100:
    BONUS_POINTS += 5
elif 100 < starter_points <= 1000:
    BONUS_POINTS += starter_points * 0.20
elif starter_points > 1000:
    BONUS_POINTS += starter_points * 0.10

if starter_points % 2 == 0:
    BONUS_POINTS += 1
elif starter_points % 10 == 5:
    BONUS_POINTS += 2

print(BONUS_POINTS)
print(starter_points + BONUS_POINTS)