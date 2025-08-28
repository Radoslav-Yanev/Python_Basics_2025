import sys

total_points = 0
max_points = -sys.maxsize
winer_name = ""

while True:
    name = input()

    points = 0

    if name == "Stop":
        break

    for char in name:
        number = int(input())

        if number == ord(char):
            points += 10

        else:
            points += 2

        if points >= max_points:
            max_points = points
            winer_name = name


print(f"The winner is {winer_name} with {max_points} points!")

