painted_eggs = int(input())

eggs_count = {"red": 0, "orange": 0, "blue": 0, "green": 0}

for _ in range(painted_eggs):
    eggs_color = input()

    if eggs_color in eggs_count:
        eggs_count[eggs_color] += 1

color, max_color = max(eggs_count.items(), key = lambda x: x[1])

print(f"Red eggs: {eggs_count['red']}")
print(f"Orange eggs: {eggs_count['orange']}")
print(f"Blue eggs: {eggs_count['blue']}")
print(f"Green eggs: {eggs_count['green']}")
print(f"Max eggs: {max_color} -> {color}")