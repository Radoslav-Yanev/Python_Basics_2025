from math import floor

points = {
    "red": {"points": 5},
    "orange": {"points": 10},
    "yellow": {"points": 15},
    "white": {"points": 20},
}

color_count = {
    "red": 0,
    "orange": 0,
    "yellow": 0,
    "white": 0,
    "black": 0,
}

balls_count = int(input())

other_count = 0
total_points = 0
result = ""

for _ in range(balls_count):
    color = input()

    if color in points:
        total_points += points[color]["points"]
        color_count[color] += 1

    elif color == "black":
        total_points = floor(total_points / 2)
        color_count[color] += 1

    else:
        other_count += 1

result += (f"Total points: {total_points}\n"
           f"Red balls: {color_count['red']}\n"
           f"Orange balls: {color_count['orange']}\n"
           f"Yellow balls: {color_count['yellow']}\n"
           f"White balls: {color_count['white']}\n"
           f"Other colors picked: {other_count}\n"
           f"Divides from black balls: {color_count['black']}")

print(result)


