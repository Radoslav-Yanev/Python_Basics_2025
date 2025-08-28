from math import ceil

WALL_COUNT = 4

wall_height = int(input())
wall_width = int(input())
no_painted_wall_percentage = int(input()) / 100

total_kv_meters = wall_height * wall_width * WALL_COUNT
kv_wall_for_paint = ceil(total_kv_meters - (total_kv_meters * no_painted_wall_percentage))

while True:
    command = input()

    if command == "Tired!":
        print(f"{kv_wall_for_paint} quadratic m left.")
        break

    paint_in_liters = int(command)
    kv_wall_for_paint -= paint_in_liters

    if kv_wall_for_paint <= 0:
        if kv_wall_for_paint < 0:
            print(f"All walls are painted and you have {abs(kv_wall_for_paint)} l paint left!")

        else:
            print("All walls are painted! Great job, Pesho!")
        break

